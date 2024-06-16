from operator import itemgetter
from langchain_core.runnables import RunnableLambda
from funcchain import chain, settings, Depends
from pydantic import BaseModel
from typing import Annotated
from .wiki_search import fetch_wiki_page

settings.llm = "azure/gpt-4o"


class Flashcard(BaseModel):
    question: str
    answer: str


class FlashcardDeck(BaseModel):
    name: str
    flashcards: list[Flashcard]


def generate_deck(
    topic: str,
    relevant_wiki_context: Annotated[
        str, Depends(itemgetter("topic") | RunnableLambda(fetch_wiki_page))
    ] = "",
) -> FlashcardDeck:
    """
    Generate a flashcard deck for the given topic.
    """
    return chain()
