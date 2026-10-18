import os
from dotenv import load_dotenv
from openai import OpenAI

# .env se key uthao
load_dotenv()

# Client setup karo (Normal sync client use kar rahe hain test ke liye)
client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print("Google Server se models ki list mangwa raha hoon...\n")

try:
    # API se models ki list fetch karo
    models = client.models.list()
    print("🎉 Yeh models tumhari API key par available hain:")
    for m in models.data:
        print(f"👉 {m.id}")
except Exception as e:
    print("🚨 Masla pakra gaya, yeh error aaya hai:")
    print(e)