import requests


def fetch_wiki_page(topic: str) -> str:
    """
    Fetch the Wikipedia page for the given topic.
    """
    try:
        wiki_link = duckduckgo_search(topic)
        if wiki_link == "":
            return ""
        jina_link = "https://r.jina.ai/" + wiki_link
        response = requests.get(jina_link, timeout=30)
        return response.text
    except Exception as e:
        print(e)
        return ""


def duckduckgo_search(query: str) -> str:
    url = "https://api.duckduckgo.com/"
    params: dict = {
        "q": "wikipedia " + query,
        "format": "json",
        "pretty": 1,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["AbstractURL"]
    else:
        return ""
