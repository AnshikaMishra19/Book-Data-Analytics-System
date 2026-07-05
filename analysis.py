import pandas as pd

# Read CSV
df = pd.read_csv("books.csv")

# Clean Price column
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

print("\n===== BOOK ANALYSIS =====")
print("Total Books:", len(df))
print("Average Price:", round(df["Price"].mean(), 2))
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())

print("\nRating Distribution:")
print(df["Rating"].value_counts())

print("\nTop 10 Most Expensive Books")
print(df.nlargest(10, "Price")[["Book Name", "Price"]])

print("\nTop 10 Cheapest Books")
print(df.nsmallest(10, "Price")[["Book Name", "Price"]])

# Save to Excel
with pd.ExcelWriter("books_analysis.xlsx") as writer:
    df.to_excel(writer, sheet_name="All Books", index=False)
    df.nlargest(10, "Price").to_excel(writer, sheet_name="Top Expensive", index=False)
    df.nsmallest(10, "Price").to_excel(writer, sheet_name="Top Cheapest", index=False)

print("\n✅ books_analysis.xlsx created successfully!")