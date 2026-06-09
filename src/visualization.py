import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("imdb_movies_2024.csv")

# Storyline length
df["Storyline_Length"] = df["Storyline"].astype(str).apply(len)

# Plot
plt.figure(figsize=(10, 5))
plt.hist(df["Storyline_Length"], bins=20)

plt.title("Distribution of Storyline Length")
plt.xlabel("Storyline Length")
plt.ylabel("Number of Movies")

plt.tight_layout()

plt.savefig("storyline_distribution.png")

plt.show()

print("Chart saved successfully!")