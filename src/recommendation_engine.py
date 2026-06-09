import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/imdb_movies_2024.csv")

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(
    df["Cleaned_Storyline"]
)

def recommend_from_storyline(
    user_storyline,
    top_n=5
):

    user_vector = tfidf.transform(
        [user_storyline]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    )

    top_indices = (
        similarity_scores.argsort()[0]
        [-top_n:][::-1]
    )

    recommendations = df.iloc[
        top_indices
    ][
        ["Movie Name", "Storyline"]
    ]

    return recommendations.reset_index(
        drop=True
    )