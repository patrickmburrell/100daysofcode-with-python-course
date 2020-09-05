import collections
from typing import List

import requests
from requests.api import request

SearchResult = collections.namedtuple(
    "SearchResult", "category, id, url, title, description"
)


def search(term: str) -> List[SearchResult]:
    url = f"http://search.talkpython.fm/api/search?q={term}"

    response = requests.get(url)
    response.raise_for_status()

    results = response.json()

    search_results = []
    for r in results.get("results"):
        search_results.append(SearchResult(**r))

    return search_results
