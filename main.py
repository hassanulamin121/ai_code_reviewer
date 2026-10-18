import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import AsyncOpenAI  # Hum Async method use karenge fast speed ke liye!

# 1. Tijori khol kar API key nikalo (.env se)
load_dotenv()

# 2. OpenAI SDK ko Gemini ke raste (endpoint) par bhejo
client = AsyncOpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 3. FastAPI ki gaari (app)
app = FastAPI(title="AI Code Reviewer API", version="1.0")

# 4. Pydantic Model (Security Guard)
class ReviewRequest(BaseModel):
    code_snippet: str
    language: str = "python"

@app.get("/")
async def root():
    return {"message": "Hassan's AI Code Reviewer is Alive and Kicking! 🚀"}

# 5. Asli AI Code Review Endpoint
@app.post("/review")
async def analyze_code(request: ReviewRequest):
    # Gemini ko message banane ka prompt
    system_prompt = f"You are an expert {request.language} code reviewer. Analyze the code for bugs, logic errors, and best practices. Give a short, professional feedback."
    
    # OpenAI SDK ke zariye Gemini ko call karna
    response = await client.chat.completions.create(
        model="gemini-3.5-flash", # Ya gemini-1.5-pro use kar sakte ho
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Here is the code to review:\n\n{request.code_snippet}"}
        ]
    )
    
    # AI ka jawab wapas return karna
    ai_feedback = response.choices[0].message.content
    
    return {
        "status": "success",
        "received_language": request.language,
        "ai_review": ai_feedback
    }