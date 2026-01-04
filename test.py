from main import scrape_page

# The URL required by Question 3
url = "https://github.com/alexeygrigorev/minsearch"

# Call the function directly
content = scrape_page(url)

# Print the length of the content
print(f"Content length: {len(content)}")