import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")

ratings = df["Rating"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(ratings.index, ratings.values)

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.savefig("ratings_graph.png")
plt.show()