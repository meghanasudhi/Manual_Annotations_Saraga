import json
import os
import compmusic
from compmusic import dunya

dunya.set_token("67a11dc1e00e22cb4bc387ee870129a819989212")
raga_dict = {}

collection = compmusic.dunya.docserver.get_collection('dunya-carnatic-cc')
for document in collection['documents']:
	mbid =  document['external_identifier']
	#print mbid 
	try:

		metadata = compmusic.dunya.carnatic.get_recording(mbid)
		for raaga in metadata['raaga']:
			raga_name = raaga['name']
			try:
				raga_list = raga_dict[raga_name]
				raga_list.append(mbid)
				print mbid,raaga['name'], 'added'
			except:
				raga_list = [mbid]
				raga_dict[raga_name] = raga_list
				print mbid,raaga['name'], 'created'

			#data = raaga['name']
			#print data 
			#print str(len(data))
			#raaga_stats = str(len()) + '\t' + raaga['name'] + '\n'
			#print raaga_stats
	except:
		print mbid

for raga in raga_dict:
	print str(len(raga_dict[raga])) + '\t' + raga  + '\n'
	#['raaga']['name']
	#print raga
