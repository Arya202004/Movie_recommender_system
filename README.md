# Movie Recommender System

## Overview

The Movie Recommender System is designed to provide personalized movie recommendations to users based on their preferences and behavior. The system utilizes machine learning algorithms, specifically content-based and collaborative filtering techniques, to analyze user data and predict movie preferences. The primary goal is to filter and predict movies that a user is most likely to enjoy, enhancing their overall viewing experience.

## Filtration Strategies

The system employs two main strategies for movie recommendation:

1. **Content-Based Filtering:**
   - Focuses on the attributes of the movies and the user's preferences.
   - Recommends movies with similar content to those the user has liked in the past.

2. **Collaborative Filtering:**
   - Analyzes user behavior and preferences.
   - Recommends movies based on the preferences of users with similar tastes.

## Implementation

The system is implemented in a Jupyter Notebook (Recommsystem.ipynb) and utilizes Python with the following libraries:

- NumPy
- Pandas

## Data

Two datasets are used in the project:

1. **Dataset.csv:**
   - Contains user-specific data, including user_id, item_id (movie id), rating, and timestamp.

2. **Movie_Id_Titles.csv:**
   - Maps movie ids to their corresponding titles.

## Data Pre-processing

The data pre-processing steps include:
- Checking for missing values and duplicates in both datasets.
- Handling missing values by dropping rows with NaN values.
- Exploring the shape and basic statistics of the datasets.

## Popularity Based Recommender System

The popularity-based recommender system focuses on recommending movies based on their popularity. Here are the key steps:

1. **Data Merging:**
   - Merges the Movie_Id_Titles.csv with Dataset.csv based on the item_id.

2. **Number of Ratings:**
   - Calculates the number of ratings received by each movie title.

3. **Average Movie Rating:**
   - Computes the average rating for each movie title.

4. **Popularity Dataset:**
   - Merges the number of ratings and average rating to create a popularity dataset.

5. **Top 20 Popular Movies:**
   - Selects the top 20 movies with the highest average ratings and a minimum of 250 ratings.

6. **Results:**
   - Displays the final list of popular movies along with their titles.

## Author

**Arya Hotey** [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/Arya202004)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/arya-hotey-aab5b32a7/)

**Aryan Paratakke** [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/Aryan152005)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aryan-paratakke-43b879276/)

## Instructions

To run the Movie Recommender System, follow these steps:

1. Ensure you have the required libraries installed: NumPy and Pandas.
2. Download the datasets: Dataset.csv and Movie_Id_Titles.csv.
3. Run the code in the provided Jupyter Notebook (Recommsystem.ipynb).

Feel free to explore and customize the code for your specific use case or dataset. For any issues or questions, please contact the project owner.

Enjoy discovering new movies with the Movie Recommender System!