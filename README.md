🤖 AI Code Reviewer

Welcome to AI Code Reviewer—an intelligent, automated code review assistant designed to act as your virtual senior software engineer. Built with a robust Python backend and powered by advanced language models, this tool scans your code, catches hidden bugs, enforces best practices, and delivers constructive, human-like feedback before your code ever hits production.

✨ Why This Exists

Code reviews are vital for maintaining software quality, but waiting on human reviews can often slow down development speed. AI Code Reviewer bridges that gap by offering instant, context-aware, and actionable code critiques. It looks beyond simple syntax errors to evaluate architecture, security vulnerabilities, edge cases, and code maintainability with the clarity and empathy of a seasoned tech lead.

🚀 Core Features

Deep Semantic & Static Analysis: Goes beyond basic linters to understand the true intent and logic of your code changes.

Prioritized Feedback: Categorizes suggestions into critical bugs, performance optimizations, security warnings, and style improvements.

Constructive, Human-Like Tone: Delivers feedback with clear explanations of the why behind every recommendation, helping developers learn and grow.

Secure & Configurable: Strict environment isolation via .env to protect your sensitive credentials.

🛠️ Tech Stack

Language: Python 3.12+

AI Engine: Google Gemini API

Validation & Config: Pydantic, Python-Dotenv

⚙️ Getting Started Locally

Follow these quick steps to get the project up and running on your machine:

1. Clone the Repository

git clone https://github.com/hassanulamin121/ai-code-reviewer.git
cd ai-code-reviewer


2. Set Up a Virtual Environment

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Configure Environment Variables

Create a .env file in the root directory of the project and add your API key:

GEMINI_API_KEY="your_actual_api_key_here"


(Note: Never push your .env file to version control!)

5. Run the Application

python main.py


🗺️ Roadmap & Future Enhancements

[ ] GitHub Webhook Integration: Automatically trigger reviews on pull requests and commits.

[ ] Custom Rules Engine: Allow developers to define custom linting/review rules via a .yaml config.

[ ] Interactive CLI Dashboard: Rich terminal UI to visualize review metrics and status.

🤝 Contributing

Contributions, ideas, and bug reports are always welcome! Feel free to fork the repository, open an issue, or submit a pull request.

Crafted with 💡 and clean code principles.
