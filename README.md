# 🤖 AI Chatbot with GPT-4 Integration using Rasa, FastAPI & PostgreSQL

This project is a hybrid AI chatbot that combines the intent classification capabilities of **Rasa** with the generative power of **GPT-4 (OpenAI)** to provide smart, dynamic responses. It also includes a backend service built using **FastAPI**, integrated with **PostgreSQL** to log user interactions for audit, review, and potential retraining.

---

## 🚀 Features

- Intent classification using Rasa NLU
- Dynamic response generation via GPT-4
- Custom Rasa actions to trigger OpenAI replies
- Backend API to serve user messages (`/chat`) using FastAPI
- PostgreSQL integration for message logging
- Response fallback handling
- Review & retraining-ready logging system

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **AI/NLP**: Rasa, OpenAI GPT-4
- **Backend**: FastAPI
- **Database**: PostgreSQL (via SQLAlchemy)
- **Tools**: Docker (optional), Uvicorn, Pydantic

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mayurpatidar1401/chatbot_backend.git
cd chatbot-backend
```

### 2. Create & Activate Virtual Environment
```bash
python3 -m venv chatbot_env
source chatbot_env/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL

-- In psql terminal
```bash
CREATE DATABASE chatbot_db;
CREATE USER chatbot_user WITH ENCRYPTED PASSWORD 'chatbot_password';
GRANT ALL PRIVILEGES ON DATABASE chatbot_db TO chatbot_user;
```
## 🚦 Run the Services

### Start FastAPI Server
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Train Rasa Model
```bash
rasa train
```

### Run Rasa Server
```bash
rasa run --enable-api --cors "*" --debug
```

### Run Action Server
```bash
rasa run actions --actions actions --debug
```

### 🧠 Intent Mapping (Sample)

    ask_gpt: Routed to GPT-4 (e.g., “What is Machine Learning?”)

    greet, goodbye: Handled with static Rasa responses

    ask_product: Custom info about your business

### 📝 Logging

All user messages and GPT/Rasa responses are logged into the user_messages table in PostgreSQL with:

    user_id

    message

    response

    timestamp

This enables review and audit for future improvement.

### 🧪 Testing GPT Access
### Run this script to validate your OpenAI key:
python test_gpt_access.py

### 📈 Future Work

    Feedback-based review system

    Auto retraining pipeline

    Sentiment-aware responses

    Multilingual support

### 🔐 API Key
### Update this line in gpt_actions.py:

openai.api_key = "your-api-key"

### 📬 Contact

For any queries, feel free to reach out or raise an issue in the repository.

👉 Check out the frontend repository here: [chatbot_frontend](https://github.com/mayurpatidar1401/chatbot-frontend)

