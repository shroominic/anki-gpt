from fastapi import FastAPI
from fastapi.responses import FileResponse
from .flashcards import generate_deck

app = FastAPI()

# Landing Page
app.get("/")(lambda: FileResponse("ankigpt/landing.html"))
app.get("/landing_image.webp")(lambda: FileResponse("ankigpt/landing_image.webp"))


@app.post("/")
async def generate_flashcards(topic: str | None = None):
    if not topic:
        return {"error": "Topic is required"}
    return generate_deck(topic)
