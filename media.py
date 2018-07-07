import webbrowser
class Movie():
	""" 
	This class provides a way to store movie related information, this class contains methods that are capable of 
	displaying the trailer in a web browser and the movie's trailer.
	"""
	VALID_RATINGS = ["G", "PG", "PG-13","R"]


	def __init__(self, title,storyline,poster_image_url,trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url


	def show_trailer(self):
		"""This function displays the trailer of the movie when called """
		webbrowser.open(self.trailer_youtube_url)

	def show_poster(self):
		"""This function displays the post of the movie when called"""
		webbrowser.open(self.poster_image_url)