from fastapi import FastAPI, HTTPException
import requests
import psycopg2
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Text, TIMESTAMP, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import traceback
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (for testing)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

DATABASE_URL = "Database URL here"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Message(Base):
    __tablename__ = "user_messages"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, index=True)
    message = Column(Text)
    response = Column(Text)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

class UserMessage(BaseModel):
    user_id: str
    message: str

def rasa_response(user_message):
    response = requests.post("http://localhost:5005/webhooks/rest/webhook", json={"message": user_message})
    return response.json()

@app.post("/chat/")
async def chat(user_msg: UserMessage):
    try:
        rasa_reply = rasa_response(user_msg.message)
        bot_response = rasa_reply[0]["text"] if rasa_reply else "I'm not sure how to respond."

        db = SessionLocal()
        new_msg = Message(user_id=user_msg.user_id, message=user_msg.message, response=bot_response)
        db.add(new_msg)
        db.commit()
        db.close()

        return {"user_message": user_msg.message, "bot_response": bot_response}
    
    except Exception as e:
        print("\n🔴 FULL ERROR LOG:")  # Print error clearly in the terminal
        traceback.print_exc()  # Print the full traceback for debugging
        raise HTTPException(status_code=500, detail=str(e))
