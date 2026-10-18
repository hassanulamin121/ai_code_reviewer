import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import AsyncOpenAI

# 1. Load environment variables from the .env file for secure key management
load_dotenv()

# 2. Initialize the asynchronous OpenAI client targeting the Google Gemini endpoint
client = AsyncOpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 3. Initialize the FastAPI application
app = FastAPI(
    title="AI Code Reviewer API",
    description="A microservice that uses AI to analyze code snippets and provide reviews.",
    version="1.0"
)

# 4. Define the request payload schema using Pydantic for validation
class ReviewRequest(BaseModel):
    code_snippet: str
    language: str = "python"

# 5. Define the POST endpoint for code review operations
@app.post("/review")
async def analyze_code_review_post(request: ReviewRequest):
    """
    Receives a code snippet, constructs a prompt, and streams it to the 
    Gemini model to get a professional code review.
    """
    # Construct the AI instruction prompt
    prompt = f"Review this {request.language} code and identify any bugs, syntax errors, or improvements:\n\n{request.code_snippet}"
    
    # Dispatch the request to the Gemini 3.5 Flash model
    response = await client.chat.completions.create(
        model="gemini-3.5-flash",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Return the structured JSON response
    return {
        "status": "success",
        "received_language": request.language,
        "ai_review": response.choices[0].message.content
    }