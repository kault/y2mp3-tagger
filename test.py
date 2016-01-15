import urllib, urllib2, json, re
import parser as p

def pretty(obj):
	return json.dumps(obj, sort_keys=True, indent=2)

def safeGet(url):
	try:
		return json.load(urllib2.urlopen(url))
	except urllib2.URLError, e:
		if hasattr(e, 'reason'):
			print "We failed to reach a server"
			print "Reason: ", e.reason
		elif hasattr(e, 'code'):
			print "The server couldn\'t fulfill the request."
			print "Error code: ", e.code
		return None 

def getDownloads(query, params={}):
	baseurl = "http://www.youtubeinmp3.com/fetch/?"
	params['format'] = 'JSON'
	params['video'] = query
	url = baseurl + urllib.urlencode(params)
	print url
	return safeGet(url)

yt_json = getDownloads("https://www.youtube.com/watch?v=F_Z_B7UQ5bU")
yt_title = yt_json["title"]

(artist, title) print artist
= p.get_artist_and_song(yt_title)
print title