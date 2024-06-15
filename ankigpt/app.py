from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
from .flashcards import generate_deck

app = FastAPI()

# Landing Page
app.get("/")(lambda: FileResponse("ankigpt/landing.html"))
app.get("/landing_image.webp")(lambda: FileResponse("ankigpt/landing_image.webp"))


@app.get("/{topic}.csv")
async def generate_flashcards(topic: str):
    if topic == "":
        raise HTTPException(status_code=400, detail="Topic is required")
    deck = generate_deck(topic)
    return Response(
        content="\n".join(
            [f"{c.question}; {c.answer}" for c in deck.flashcards],
        ),
        media_type="text/csv",
    )
