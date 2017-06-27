import json
import os
import compmusic
from compmusic import dunya

dunya.set_token("67a11dc1e00e22cb4bc387ee870129a819989212")
concert_dict = {}

collection = compmusic.dunya.docserver.get_collection('dunya-carnatic-cc')
for document in collection['documents']:
	mbid =  document['external_identifier']
	#print mbid 
	try:

		metadata = compmusic.dunya.carnatic.get_recording(mbid)
		for concert in metadata['concert']:
			concert_title = concert['title']
			try:
				concert_list = concert_dict[concert_title]
				concert_list.append(mbid)
				print mbid,concert['title'], 'added'
			except:
				concert_list = [mbid]
				concert_dict[concert_title] = concert_list
				print mbid,concert['title'], 'created'

			#data = concert['title']
			#print data 
			#print str(len(data))
			#concert_stats = str(len()) + '\t' + concert['title'] + '\n'
			#print concert_stats
	except:
		print mbid

for concert in concert_dict:
	print str(len(concert_dict[concert])) + '\t' + concert  + '\n'