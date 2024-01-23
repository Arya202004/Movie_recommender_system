
# Movie Recommender System

## Overview

The Movie Recommender System is a collaborative project aimed at providing users with personalized movie recommendations. The system utilizes machine learning algorithms to filter and predict movies based on user preferences. Two main filtration strategies have been implemented:

1. **Popularity-Based Filtering:**
   - Recommends movies based on their popularity and average ratings.
   - Utilizes the number of ratings and average rating for each movie title.

2. **Collaborative Filtering:**
   - Analyzes user behavior and recommends movies based on the preferences of similar users.
   - Employs cosine similarity and matrix factorization methods for generating recommendations.

## Code and Implementation

### [movie-recommender-system.ipynb](https://github.com/Arya202004/Movie_recommender_system/blob/main/movie-recommender-system.ipynb)

#### 1. Initialization

The notebook begins by importing necessary libraries such as NumPy, Pandas, scikit-learn, and loading the dataset ([`Dataset.csv`](https://github.com/Arya202004/Movie_recommender_system/tree/main/Dataset) and [`Movie_Id_Titles.csv`](https://github.com/Arya202004/Movie_recommender_system/tree/main/Dataset)).

#### 2. Data Pre-processing

This section focuses on ensuring data quality by checking for missing values and duplicates in the datasets. Missing values are handled by dropping rows with NaN values, and unnecessary columns (e.g., timestamp) are removed.

#### 3. Popularity-Based Recommender System

   - **Merging Datasets:** Movie titles are merged with the dataset based on item_id.
   - **Number of Ratings:** Calculates the number of ratings and average rating for each movie title.
   - **Generating Popularity Dataset:** Merges the number of ratings and average rating to create a popularity dataset.
   - **Selecting Top 20 Popular Movies:** Filters movies with a minimum of 250 ratings and sorts them by average rating in descending order.

#### 4. Collaborative Filtering Recommender System

   - **Identifying Experienced Users:** Users with a minimum of 200 ratings are identified.
   - **Selecting Popular Movies:** Movies with a minimum of 50 ratings are selected.
   - **Creating Pivot Table:** A pivot table is created for collaborative filtering with users, movies, and ratings.
   - **Cosine Similarity:** Cosine similarity is used to measure the similarity between movies.
   - **Recommendation Function:** A `recommend` function is defined to provide movie suggestions based on user preferences.

### Instructions for Usage

To use the Movie Recommender System:

1. Run the Jupyter Notebook `movie-recommender-system.ipynb`.
2. Ensure the required libraries (NumPy, Pandas, scikit-learn) are installed ([check requirements.txt]()).
3. Download the datasets: `Dataset.csv` and `Movie_Id_Titles.csv`.
4. Explore and customize the code for specific use cases or datasets.

## Author

**Arya Hotey** [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/Arya202004)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/arya-hotey-aab5b32a7/)

**Aryan Paratakke** [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/Aryan152005)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aryan-paratakke-43b879276/)

Feel free to contact for any questions or improvements to the Movie Recommender System. Enjoy discovering new movies with the recommendations!
