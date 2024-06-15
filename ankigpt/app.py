from fastapi import FastAPI
from .flashcards import generate_deck

app = FastAPI()


@app.get("/")
async def generate(topic: str | None = None):
    if not topic:
        return {"error": "Topic is required"}
    return generate_deck(topic)
