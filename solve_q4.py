from main import scrape_page

# 1. Define the URL
url = "https://datatalks.club/"

# 2. Use your tool to get the content
# Note: Since we are running this as a script, we call the function directly.
# If 'scrape_page' is decorated with @mcp.tool, it might be wrapped.
# If you split it into 'scrape_page_logic' as discussed before, use that.
# Otherwise, the FastMCP decorator usually allows direct calls for testing.
content = scrape_page(url)

# 3. Count the word "data" (case-insensitive)
word_to_find = "data"
count = content.lower().count(word_to_find)

print(f"The word '{word_to_find}' appears {count} times.")