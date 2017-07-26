import webbrowser


class Movie():

	''' Yo, this is my own class and you can build any instances using this class '''
	
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): #this function initialize a object
		self.title = movie_storyline
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		


	def show_trailer(self):                             #this instance method can open a youtube url to show trailer
		webbrowser.open(self.trailer_youtube_url)

