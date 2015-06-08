__author__ = 'ned'

import media
import fresh_tomatoes

# Create indivdual movies by calling media.Movie with proper attributes
toy_story = media.Movie("Toy Story",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                         "G",
                         "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.")

avatar = media.Movie("Avatar",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                      "PG-13",
                      "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.")

hangover = media.Movie("The Hangover",
                        "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                        "https://www.youtube.com/watch?v=vhFVZsk3XEs",
                        "R",
                        "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.")

# Create list of movies
movie_list = [toy_story, avatar, hangover]

# Pass list of movies to open_movies_page function in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movie_list)