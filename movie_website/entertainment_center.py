import media
import fresh_tomatoes
import requests
import json


####################################################
##Title: ML project two
##Name: Ruozhen Gu
##Date: July 2, 2017
##University: University of Waterloo
##Contact: gu.gabriel@hotmail.com
####################################################


## obtain_movie_info(): consumes nothing but returns a list of movie info by requesting an api for 
##    each of the movies from website The Movie DB
## Effects: the function mutates list info to contain all necessary movie information
def obtain_movie_info():
	candidates = ['297762','321612', '260514', '335988']
	info = []
	for i in range(4):
		api_url = "https://api.themoviedb.org/3/movie/" + candidates[i] + "?api_key=68ba47b267a750494d9a254a75fc73db" 
		movie_info = requests.get(api_url)                      #request api
		jdata = movie_info.json()	                            #convert into json format
		movie_title = jdata['original_title']	                #retrieve title information
		movie_overview = jdata['overview']		                #retrieve overview
		info.append([movie_title, movie_overview])	            #mutate info to contain those information
	return info



## obtain_poster_url(): consumes nothing but returns a list of poster url by requesting an api for 
##    each of the movies from website The Movie DB
## Effects: the function mutates list info to contain all necessary poster url
def obtain_poster_url():
	candidates = ['297762', '321612', '260514', '335988']
	url_images = []

	''' the following three lines is to get the base url by requesting an api '''
	image = requests.get("https://api.themoviedb.org/3/configuration?api_key=68ba47b267a750494d9a254a75fc73db") #sending request for api configuration
	jdata = image.json()																						
	base_url = jdata['images']['base_url'] #retrieve base_url

	for i in range(4):
		api_url = "https://api.themoviedb.org/3/movie/" + candidates[i] + "/images?api_key=68ba47b267a750494d9a254a75fc73db"
		poster_info = requests.get(api_url)
		jdata = poster_info.json()
		path = jdata['backdrops'][0]['file_path']						#retrieve file_path or poster path
		url = url_321612 = base_url + 'w500' + path                     #obtain actual url path
		url_images.append(url)											#mutate url_images to contain all information
	return url_images



## obtain_youtube_url(): consumes nothing but returns a list of movie trailer url on youtube by requesting an api for 
##    each of the movies from website The Movie DB
## Effects: the function mutates list info to contain all necessary movie trailer url
def obtain_youtube_url():
	candidates = ['297762', '321612', '260514', '335988']
	youtube_url = []
	youtube_base_url = "https://youtu.be/"
	for i in range(4):
		api_url = "https://api.themoviedb.org/3/movie/" + candidates[i] + "/videos?api_key=68ba47b267a750494d9a254a75fc73db&language=en-US"
		video_info = requests.get(api_url)				#request api
		jdata = video_info.json()
		key = jdata['results'][0]['key']				#retrieve key 
		url_path = youtube_base_url + key 				#obtain actual url_path
		youtube_url.append(url_path)					#mutate youtube_url to contain necessary information
	return youtube_url



## build_instances(): consumes nothing and builds four movie instances with their fields by calling three helper functions. 
##	eventually the function calls fresh_tomatoes and open a web page

def build_instances():

	''' fetch all necessary information for instances' fields '''
	info = obtain_movie_info()
	images = obtain_poster_url()
	trailers = obtain_youtube_url()
	

	''' build four instances of class Movie '''
	Wonder_woman = media.Movie(info[1][0].encode('ascii', 'ignore'), 
							   info[1][1].encode('ascii', 'ignore'), 
							   images[1].encode('ascii', 'ignore'), 
							   trailers[1].encode('ascii', 'ignore'))



	Beauty_and_the_beast = media.Movie(info[0][0].encode('ascii', 'ignore'), #encode function helps compiler ignores unrecognized ASCII char
									   info[0][1].encode('ascii', 'ignore'),
									   images[0].encode('ascii', 'ignore'), 
									   trailers[0].encode('ascii', 'ignore'))
							
	

	Cars_3 = media.Movie(info[2][0].encode('ascii', 'ignore'), 
						 info[2][1].encode('ascii', 'ignore'), 
						 images[2].encode('ascii', 'ignore'), 
						 trailers[2].encode('ascii', 'ignore'))

	Transformer = media.Movie(info[3][0].encode('ascii', 'ignore'), 
							  info[3][1].encode('ascii', 'ignore'), 
						      images[3].encode('ascii', 'ignore'), 
							  trailers[3].encode('ascii', 'ignore'))

	movies = [Beauty_and_the_beast, Wonder_woman, Cars_3, Transformer]

	''' call fresh_tomatoes which contains html source code and open the web page '''

	fresh_tomatoes.open_movies_page(movies)

print media.Movie.__doc__


build_instances()   #execute


