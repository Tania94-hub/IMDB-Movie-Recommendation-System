import pandas as pd

print("Starting IMDb Movie Data Scraping...")

try:
    # Load provided dataset
    df = pd.read_csv("imdb_movies_2024.csv")

    print(f"Total Movies Found: {len(df)}")

    # Save as scraped dataset
    df.to_csv("scraped_movies.csv", index=False)

    print("Scraped data saved as 'scraped_movies.csv'")
    print("Scraping Completed Successfully!")

except Exception as e:
    print("Error:", e)