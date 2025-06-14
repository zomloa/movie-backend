# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link 

db = SessionLocal()

# %%
# Tester la récupération de quelques films
movies = db.query(Movie).limit(10).all()
for movie in movies:
    print(f"ID : {movie.movieId}, Titre : {movie.title}, Genre : {movie.genres}")
else:
    print("No movies found")

# %%
# Récupérer les films du genre action
action_movies = db.query(Movie).filter(Movie.genres.like("%Action%")).limit(5).all()
for movie in action_movies:
    print(f"ID : {movie.movieId}, Titre : {movie.title}, Genre : {movie.genres}")



# %%
# Tester la récupération de quelques évaluations (ratings)
Ratings = db.query(Rating).limit(5).all()
for rating in Ratings:
     print(f"User ID : {rating.userId}, Movie ID : {rating.movieId}, Rating : {rating.rating} Timestamp : {rating.timestamp}")
# %%
# Film donc la note est supérieur à 4
hight_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating>=4, Movie.movieId==Rating.movieId)
    .limit (5)
    .all()
)
print(hight_rated_movies)
for title, rating in hight_rated_movies:
    print(title, rating)

# %%
# Récupération des tags associés au film
hight_tag_movies = (
    db.query(Movie.title, Tag.tag)
    .join(Tag)
    .limit(5)
    .all()
)
print(hight_tag_movies)
for title, tag in hight_tag_movies:
    print(title, tag)
# %%
# Tester la classe link
links = db.query(Link).limit(5).all()
for link in links :
    print(f"Movie ID : {link.movieId}, IMDB : {link.imdbId}, TMDB : {link.tmdbId}")
# %%
# Fermeture à la BD
db.close()
# %%
# Tester 