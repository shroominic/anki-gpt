import re
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
        short_response_text = response.text
        trimmed_response = trim_after_substring(short_response_text,"References\[[edit](")
        cleaned_string = remove_html_tags(trimmed_response)
        return cleaned_string
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


def trim_after_substring(original_string, substring):
    # Find the position of the substring in the original string
    pos = original_string.find(substring)

    # Check if the substring was found
    if pos != -1:
        # Trim the string after the found position
        return original_string[:pos]
    else:
        # If the substring is not found, return the original string
        return original_string


def remove_html_tags(text):
    # Regular expression to match HTML tags
    clean = re.compile(r'<.*?>')
    # Replace matched HTML tags with an empty string
    return re.sub(clean, '', text)
