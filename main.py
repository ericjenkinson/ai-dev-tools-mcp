from fastmcp import FastMCP
import requests

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

if __name__ == "__main__":
    mcp.run()
