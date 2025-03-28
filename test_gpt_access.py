import openai

openai.api_key = "Open AI API Key" # Use your actual OpenAI API key here

try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello GPT-4, can you reply?"}]
    )
    print(response["choices"][0]["message"]["content"])
except Exception as e:
    print("❌ Error:", e)
