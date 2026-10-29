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
