# 🧠 Trivia Question Generator API

A simple, containerized FastAPI application that generates trivia questions using OpenAI’s GPT model. The API allows users to specify a category and difficulty level, and returns a JSON response with a generated question and answer.

This mini-project was built to practice skills relevant to roles involving API development, LLM integration, and cloud-readiness—like the engineering role at Adaly.

---

## 🚀 Features

- 🔌 **FastAPI** RESTful API with automatic Swagger docs
- 🤖 **LLM Integration** using OpenAI’s GPT (ChatCompletion API)
- 🧪 **Structured Input/Output** using Pydantic data models
- 🐳 **Dockerized** for easy cloud deployment
- 🔐 **Environment Variable Management** with `python-dotenv`

---

## 🛠️ Tech Stack

| Tool        | Purpose |
|-------------|---------|
| **FastAPI** | Async web framework for building high-performance APIs |
| **OpenAI API** | Generates trivia questions using GPT-3.5 |
| **Python-dotenv** | Loads API keys securely from `.env` files |
| **Docker**   | Packages the app in a container for portable deployment |
| **Uvicorn**  | ASGI server to run the FastAPI app |

---

## 📦 How to Run Locally

### 🧱 Step 1: Install Dependencies

```bash pip install -r requirements.txt```

### 2. Create .env File
Create a file named ```.env``` in the root directory of your project and paste in your OpenAI API key:
```OPENAI_API_KEY=your_openai_key_here```


### 3. Start the App

```uvicorn main:app --reload```

```http://localhost:8000/docs```
