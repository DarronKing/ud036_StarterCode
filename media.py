import webbrowser


class Movie():

    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Function defining our movie
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Assigning our .self values to the instance values.
        # This makes so we can freely call them.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function opening our trailer
    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
