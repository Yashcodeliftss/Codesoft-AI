import pandas as pd
from sklearn.neighbors import NearestNeighbors


movies = pd.read_csv('ml-latest-small/movies.csv')
ratings = pd.read_csv('ml-latest-small/ratings.csv')


print("Movies Dataset:")
print(movies.head())
print("\nRatings Dataset:")
print(ratings.head())


user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')


user_item_matrix.fillna(0, inplace=True)


print("\nUser-Item Matrix:")
print(user_item_matrix.head())


model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(user_item_matrix)


def get_movie_recommendations(user_id, num_recommendations=5):
    user_index = user_id - 1  
    distances, indices = model.kneighbors(user_item_matrix.iloc[user_index, :].values.reshape(1, -1), n_neighbors=num_recommendations + 1)
    
    
    similar_users_indices = indices.flatten()
    
   
    movie_ids = []
    for i in range(1, len(similar_users_indices)):
        similar_user_index = similar_users_indices[i]
        similar_user_ratings = user_item_matrix.iloc[similar_user_index]
        top_movie_ids = similar_user_ratings.sort_values(ascending=False).index.tolist()
        movie_ids.extend(top_movie_ids)
    
   
    movie_ids = list(set(movie_ids))
    watched_movie_ids = user_item_matrix.columns[user_item_matrix.iloc[user_index] > 0].tolist()
    recommended_movie_ids = [movie_id for movie_id in movie_ids if movie_id not in watched_movie_ids]
    
   
    top_recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)].head(num_recommendations)
    return top_recommended_movies


user_id = 1
recommended_movies = get_movie_recommendations(user_id)
print("\nRecommended Movies for User {}:".format(user_id))
print(recommended_movies)
