import re

regex_pattern = '(.*) - (.*)'

def get_artist_and_song(yt_title):
	'''
	Returns tuple of title and artist
	'''
	matches = re.findall(regex_pattern, yt_title, re.DOTALL)
	title = matches[0][0]
	artist = matches[0][1]

	return (title, artist)