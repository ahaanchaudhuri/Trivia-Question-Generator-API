from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import openai
import json
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()
app = FastAPI()

class TriviaRequest(BaseModel):
    category: str
    difficulty: str  # easy, medium, hard

@app.get("/")
async def root():
    return {"message": "Trivia Generator API is running."}

@app.post("/generate-question/")
async def generate_question(request: TriviaRequest):
    try:
        question, answer = await create_trivia_question(request.category, request.difficulty)
        return {
            "category": request.category,
            "difficulty": request.difficulty,
            "question": question,
            "answer": answer
        }
    except Exception as e:
        return {"error": str(e)}

async def create_trivia_question(category: str, difficulty: str):
    prompt = (f"Create a trivia question for the category: {category} and difficulty: {difficulty}. Return the question and answer in a JSON format.")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    qa_pair = json.loads(response.choices[0].message.content)
    return qa_pair["question"], qa_pair["answer"]

