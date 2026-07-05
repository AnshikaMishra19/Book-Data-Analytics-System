import pandas as pd

# Load CSV
df = pd.read_csv("books.csv")

# User input
book = input("Enter Book Name: ")

# Search book (case-insensitive)
result = df[df["Book Name"].str.contains(book, case=False, na=False)]

if result.empty:
    print("\n❌ Book Not Found")
else:
    for _, row in result.iterrows():
        price = str(row["Price"]).replace("Â£", "£")
        availability = str(row["Availability"]).replace("Â", "").strip()

        print("\n-----------------------------")
        print("📖 Book Name   :", row["Book Name"])
        print("💰 Price       :", price)
        print("⭐ Rating      :", row["Rating"])
        print("📦 Availability:", availability)
        print("-----------------------------")