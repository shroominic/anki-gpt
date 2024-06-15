from funcchain import chain
from pydantic import BaseModel


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
