import streamlit as st
from src.recommendation_engine import recommend_from_storyline

# Page Configuration
st.set_page_config(
    page_title="IMDB Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Title
st.title("🎬 IMDB Movie Recommendation System")

st.write(
    "Enter a movie storyline and get the Top 5 recommended movies."
)

# User Input
storyline = st.text_area(
    "Enter Storyline",
    height=200
)

# Recommendation Button
if st.button("Recommend Movies"):

    if storyline.strip() == "":
        st.warning("Please enter a storyline.")

    else:

        results = recommend_from_storyline(storyline)

        st.success("Top 5 Recommended Movies")

        for i, row in results.iterrows():

            st.markdown(
                f"## 🎬 {row['Movie Name']}"
            )

            st.info(
                row['Storyline']
            )

            st.markdown("---")