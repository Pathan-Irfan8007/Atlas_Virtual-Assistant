import re
import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="Atlas/1.0 (atlas@example.com)",
    language="en"
)

def wikipedia_answer(query, sentences=1):
    for phrase in [
        "what is",
        "who is",
        "tell me about",
        "define",
        "search wikipedia for",
    ]:
        query = query.lower().replace(phrase, "").strip()

    page = wiki.page(query.title())

    if not page.exists():
        return "Sorry, I couldn't find anything on Wikipedia."

    summary = page.summary
    sentence_list = re.split(r'(?<=[.!?])\s+', summary)

    return " ".join(sentence_list[:sentences])


# print(wikipedia_answer("what is force"))