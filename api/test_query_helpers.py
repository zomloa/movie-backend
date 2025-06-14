from database import SessionLocal
from query_helpers import *

db = SessionLocal()

# movies = get_movies(db, limit =5)
# for movie in movies:
  #  print(f"ID : {movie.movieId}, Titre : {movie.title}, Genre : {movie.genres}")

# rating = get_rating(db, movie_id= 1, user_id= 1)
# print(f"User ID : {rating.userId}, Movie ID : {rating.movieId}, Rating : {rating.rating}, Timestamp : {rating.timestamp}")

n_movies = get_link_count(db)
print(f"Nombre d'évaluations : {n_movies}")
db.close()