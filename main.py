from fastmcp import FastMCP
import requests
from typing import List, Dict

# import the search utilities we added
from search import collect_docs_from_zips, build_index, search_index

mcp = FastMCP("Demo 🚀")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool
def scrape_page(url: str) -> str:
    """Scrape a web page using Jina Reader"""
    # Jina Reader URL prefix
    jina_url = f"https://r.jina.ai/{url}"

    # specific user agent to ensure we get a clean response (good practice)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(jina_url, headers=headers)
    return response.text


# Lazy-built index cached in module
INDEX = None


def ensure_index() -> None:
    """Builds the minsearch index from ZIP files in the current directory on demand."""
    global INDEX
    if INDEX is not None:
        return
    docs = collect_docs_from_zips('.')
    if not docs:
        INDEX = None
        return
    INDEX = build_index(docs)


@mcp.tool
def search_docs(query: str, top_n: int = 5) -> List[Dict]:
    """Search indexed markdown/mdx documents and return top results.

    Returns a list of dicts with `filename` and `snippet`.
    """
    ensure_index()
    if INDEX is None:
        return []
    results = search_index(INDEX, query, top_n)
    out = []
    for r in results:
        snippet = (r.get('content') or '')[:300]
        out.append({'filename': r.get('filename'), 'snippet': snippet})
    return out


if __name__ == "__main__":
    mcp.run()
