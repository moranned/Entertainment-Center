__author__ = 'ned'

class Movie():
  """ This class provides a means to store movie related information
  """

  # Movie class constructor. Defines attributes of a movie
  def __init__(self, title, poster_image_url, trailer_youtube_url, rating, description):
    self.title = title
    self.poster_image_url = poster_image_url
    self.trailer_youtube_url = trailer_youtube_url
    self.rating = rating
    self.description = description