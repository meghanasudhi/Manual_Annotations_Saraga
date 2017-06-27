import json
import os
import compmusic
from compmusic import dunya

dunya.set_token("67a11dc1e00e22cb4bc387ee870129a819989212")
album_artists_dict = {}

collection = compmusic.dunya.docserver.get_collection('dunya-carnatic-cc')
for document in collection['documents']:
	mbid =  document['external_identifier']
	#print mbid 
	try:

		metadata = compmusic.dunya.carnatic.get_recording(mbid)
		for album_artists in metadata['album_artists']:
			album_artists_name = album_artists['name']
			try:
				album_artists_list = album_artists_dict[album_artists_name]
				album_artists_list.append(mbid)
				print mbid,album_artists['name'], 'added'
			except:
				album_artists_list = [mbid]
				album_artists_dict[album_artists_name] = album_artists_list
				print mbid,album_artists['name'], 'created'

			#data = album_artists['name']
			#print data 
			#print str(len(data))
			#album_artists_stats = str(len()) + '\t' + album_artists['name'] + '\n'
			#print album_artists_stats
	except:
		print mbid

for album_artists in album_artists_dict:
	print str(len(album_artists_dict[album_artists])) + '\t' + album_artists  + '\n'