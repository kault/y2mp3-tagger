import re

regex_pattern = '(.*) - (.*)'

def get_artist_and_song(yt_title):
	matches = re.findall(regex_pattern, yt_title, re.DOTALL)
	print matches