# 🚀 AI Code Reviewer Microservice

An AI-powered microservice that analyzes code snippets, identifies bugs, security vulnerabilities, and performance bottlenecks, and provides structured, human-like feedback. 

Built with **FastAPI** and powered by **Google Gemini API** (using the OpenAI SDK compatibility layer).

---

## 📌 Key Features

- **🧠 AI-Powered Analysis:** Goes beyond basic syntax checking. It analyzes architecture, security, edge cases, and maintainability.
- **📑 Categorized Feedback:** The AI structures its response into Critical Bugs, Security Warnings, Performance Optimizations, and Style suggestions.
- **⚡ Asynchronous Architecture:** Built with `AsyncOpenAI` and FastAPI for non-blocking, high-performance I/O operations.
- **🔒 Secure Key Management:** API keys are strictly isolated using `.env` files and are never hardcoded.
- **📖 Auto-Generated Docs:** Comes with built-in Swagger UI for easy testing and interaction.
- **🐳 Dockerized:** Fully containerized for seamless deployment across any environment.

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI
- **AI Engine:** Google Gemini API (via OpenAI Python SDK)
- **Data Validation:** Pydantic
- **Environment Management:** python-dotenv
- **Deployment:** Docker & Uvicorn

---

## 🏗️ Architecture / Flow

1. **Request:** User sends a code snippet via a POST request.
2. **Validation:** Pydantic validates the incoming payload (ensuring the code field exists).
3. **AI Processing:** The FastAPI endpoint uses AsyncOpenAI (configured with Gemini's base URL) to send the code and a custom prompt to the Gemini model.
4. **Response:** The AI returns a structured review, which is parsed and sent back to the user.

---

## ⚙️ Step-by-Step Setup Guide

Follow these instructions sequentially to get the project running on your local machine.

### Prerequisites
Make sure you have installed:
- Python 3.12+
- Git
- Docker Desktop (Optional, if you want to run it via Docker)

---

### Step 1: Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/hassanulamin121/ai_code_reviewer.git
cd ai_code_reviewer

Step 2: Get your Gemini API Key
Go to Google AI Studio (https://aistudio.google.com/).

Click on "Get API Key" and create a new API key.

Copy the key. (Never share this key publicly or commit it to GitHub).

Step 3: Configure Environment Variables
Create a file named .env in the root directory of the project. Open it and paste your API key:

env
GEMINI_API_KEY="your_actual_api_key_here"

Step 4: Run Locally (Without Docker)
If you want to run the project directly on your machine:

Create and Activate Virtual Environment:
Windows:

bash
python -m venv venv
venv\Scripts\activate

macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate

Install Dependencies:

bash
pip install -r requirements.txt
Run the Application:

bash
uvicorn main:app --reload

Step 5: Run with Docker (Alternative Method)
If you prefer using Docker, ensure Docker Desktop is running in the background.

Build the Docker Image:

bash
docker build -t ai-code-reviewer .

Run the Docker Container:
Pass the .env file securely to the container and map the ports:

bash
docker run -d -p 8000:8000 --env-file .env --name code-reviewer-container ai-code-reviewer

🚀 How to Use / Test the API
Once the application is running (either via Local or Docker), follow these steps:

Open your browser and go to: http://127.0.0.1:8000/docs

You will see the FastAPI Swagger UI.

Expand the POST /analyze_code_review_post endpoint.

Click on the "Try it out" button.

Paste your code snippet in the JSON payload box. Example:

json
{
  "code": "def add(a, b):\n    return a + b"
}
Click "Execute" and scroll down to see the AI's response!

🛡️ Security Best Practices
Never hardcode your API keys directly in the Python code.

Ensure .env is always listed in your .gitignore file.

If you accidentally commit an API key to GitHub, revoke it immediately via Google AI Studio and generate a new one.

Built with ❤️ for the developer community.





