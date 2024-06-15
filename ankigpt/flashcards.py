from funcchain import chain, settings
from pydantic import BaseModel

settings.llm = "azure/gpt-4o"


class Flashcard(BaseModel):
    question: str
    answer: str


class FlashcardDeck(BaseModel):
    name: str
    flashcards: list[Flashcard]


def generate_deck(topic: str) -> FlashcardDeck:
    """
    Generate a flashcard deck for the given topic.
    """
    return chain()
