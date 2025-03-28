import openai
from rasa_sdk import Action

openai.api_key = "Open AI API Key" # Use your actual OpenAI API key here

class ActionGPT4Response(Action):
    def name(self):
        return "action_gpt4_response"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text")
        print(f"✅ Registered action: action_gpt4_response")
        print(f"🔍 Calling GPT-4 with: {user_message}")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": user_message}]
            )
            bot_reply = response["choices"][0]["message"]["content"]
            print(f"🤖 GPT-4: {bot_reply}")
            dispatcher.utter_message(text=bot_reply)
        except Exception as e:
            print(f"❌ Error calling GPT-4: {type(e).__name__} - {e}")
            dispatcher.utter_message(text="Sorry, I couldn't get a response from GPT-4.")
        return []