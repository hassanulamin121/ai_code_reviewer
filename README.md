🚀 AI Code Reviewer Microservice
An AI-powered microservice that analyzes code snippets, identifies bugs, security vulnerabilities, and performance bottlenecks, and provides structured, human-like feedback.

Built with FastAPI and powered by Google Gemini API (using the OpenAI SDK compatibility layer).

✨ Key Features
🧠 AI-Powered Analysis: Goes beyond basic syntax checking. It analyzes architecture, security, edge cases, and maintainability.

📑 Categorized Feedback: The AI structures its response into Critical Bugs, Security Warnings, Performance Optimizations, and Style suggestions.

⚡ Asynchronous Architecture: Built with AsyncOpenAI and FastAPI for non-blocking, high-performance I/O operations.

🔒 Secure Key Management: API keys are strictly isolated using .env files and are never hardcoded.

📖 Auto-Generated Docs: Comes with built-in Swagger UI for easy testing and interaction.

🐳 Dockerized: Fully containerized for seamless deployment across any environment.

🛠️ Tech Stack
Backend Framework: FastAPI

AI Engine: Google Gemini API (via OpenAI Python SDK)

Data Validation: Pydantic

Environment Management: python-dotenv

Deployment: Docker & Uvicorn

🏗️ Architecture / Flow
Request: User sends a code snippet via a POST request.

Validation: Pydantic validates the incoming payload (ensuring the code field exists).

AI Processing: The FastAPI endpoint uses AsyncOpenAI (configured with Gemini's base URL) to send the code and a custom prompt to the Gemini model.

Response: The AI returns a structured review, which is parsed and sent back to the user.

⚙️ Step-by-Step Setup Guide
Follow these instructions to get the project running on your local machine.

Prerequisites
Make sure you have installed:

Python 3.12+

Git

Docker Desktop (Optional, for Docker setup)

🔑 Step 1: Get your Gemini API Key
Go to Google AI Studio.

Click on "Get API Key" and create a new API key.

Copy the key. (Note: Never share this key or commit it to GitHub).

💻 Method A: Running Locally (Without Docker)
1. Clone the Repository
git clone https://github.com/hassanulamin121/ai_code_reviewer.git
cd ai_code_reviewer
.
2. Create and Activate Virtual Environment
Windows:

python -m venv venv
venv\Scripts\activate
.
macOS/Linux:
python3 -m venv venv
source venv/bin/activate
.
3. Install Dependencies
pip install -r requirements.txt
.
4. Setup Environment Variables
Create a .env file in the root directory and add your API key:
GEMINI_API_KEY="your_actual_api_key_here"
.
5. Run the Application
uvicorn main:app --reload
.

🐳 Method B: Running with Docker (Recommended)
Ensure Docker Desktop is running in the background.

1. Clone the Repository

bash
git clone https://github.com/hassanulamin121/ai_code_reviewer.git
cd ai_code_reviewer
2. Setup Environment Variables
Create a .env file in the root directory:

env
GEMINI_API_KEY="your_actual_api_key_here"
3. Build the Docker Image

bash
docker build -t ai-code-reviewer .
4. Run the Docker Container
Pass the .env file securely to the container and map the ports:

bash
docker run -d -p 8000:8000 --env-file .env --name code-reviewer-container ai-code-reviewer
🚀 How to Use
Once the application is running (either via Local or Docker):

Open your browser and go to: http://127.0.0.1:8000/docs

You will see the FastAPI Swagger UI.

Expand the POST /analyze_code_review_post endpoint.

Click "Try it out".

Paste your code snippet in the JSON payload:

json
{
  "code": "def add(a, b):\n    return a + b"
}
Click "Execute" and scroll down to see the AI's response!

🛡️ Security Note
Never hardcode your API keys in the code.

Ensure .env is listed in your .gitignore file.

If you accidentally commit a key, revoke it immediately via Google AI Studio.

Built with ❤️ for the developer community.

