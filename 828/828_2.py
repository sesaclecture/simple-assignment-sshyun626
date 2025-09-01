movies = {
    "Action": ["Die Hard", "Mad Max", "John Wick"],
    "Comedy": ["Superbad", "Step Brothers", "The Hangover"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"]
}

genre = input("What genre do you prefer? (Action, Comedy, Drama)")

if genre in movies:
    print(f"Recommended {genre} movies: {', '.join(movies[genre])}")
else:
    print("Sorry, we don't have recommendations for that genre.")
