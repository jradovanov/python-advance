def movie_organizer(*args):
    genres = {}

    # Group movies by genre
    for movie in args:
        name, genre = movie
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(name)

    # Sort genres by the number of movies (descending) and genre name (ascending)
    sorted_genres = sorted(genres.items(), key=lambda x: (-len(x[1]), x[0]))

    # Print the output
    for genre, movies in sorted_genres:
        print(f"{genre} - {len(movies)}")
        sorted_movies = sorted(movies)
        for movie in sorted_movies:
            print(f"* {movie}")


# Test cases
movie_organizer(
    ("The Matrix", "Sci-fi")
)

movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")
)
