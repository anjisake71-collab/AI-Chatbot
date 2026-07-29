from ddgs import DDGS


def web_search(query: str, max_results: int = 5):
    try:
        results = DDGS().text(
            query,
            max_results=max_results
        )

        return [
            {
                "title": item.get("title", ""),
                "url": item.get("href", ""),
                "snippet": item.get("body", "")
            }
            for item in results
        ]

    except Exception as e:
        print("Web search error:", e)
        return []  