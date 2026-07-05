import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1, 51):   # Total 50 pages

    print(f"Scraping Page {page}...")

    url = base_url.format(page)

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Page {page} not found.")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = (
    book.find("p", class_="price_color")
    .text.replace("Â£", "£")
    .replace("£", "")
)

        rating = book.find("p")["class"][1]

        availability = "In Stock"

        data.append({
            "Book Name": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

df = pd.DataFrame(data)

df.to_csv("books.csv", index=False, encoding="utf-8-sig")

print("\n✅ Total Books Scraped:", len(df))