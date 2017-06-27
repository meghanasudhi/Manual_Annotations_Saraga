import json
import os
import compmusic
from compmusic import dunya

dunya.set_token("67a11dc1e00e22cb4bc387ee870129a819989212")
taala_dict = {}

collection = compmusic.dunya.docserver.get_collection('dunya-carnatic-cc')
for document in collection['documents']:
	mbid =  document['external_identifier']
	#print mbid 
	try:

		metadata = compmusic.dunya.carnatic.get_recording(mbid)
		for taala in metadata['taala']:
			taala_name = taala['name']
			try:
				taala_list = taala_dict[taala_name]
				taala_list.append(mbid)
				print mbid,taala['name'], 'added'
			except:
				taala_list = [mbid]
				taala_dict[taala_name] = taala_list
				print mbid,taala['name'], 'created'

			#data = taala['name']
			#print data 
			#print str(len(data))
			#taala_stats = str(len()) + '\t' + taala['name'] + '\n'
			#print taala_stats
	except:
		print mbid

for taala in taala_dict:
	print str(len(taala_dict[taala])) + '\t' + taala  + '\n'