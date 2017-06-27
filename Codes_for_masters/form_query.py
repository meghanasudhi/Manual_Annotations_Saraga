import json
import os
import compmusic
from compmusic import dunya

dunya.set_token("67a11dc1e00e22cb4bc387ee870129a819989212")
form_dict = {}

collection = compmusic.dunya.docserver.get_collection('dunya-carnatic-cc')
for document in collection['documents']:
	mbid =  document['external_identifier']
	#print mbid 
	try:

		metadata = compmusic.dunya.carnatic.get_recording(mbid)
		for form in metadata['form']:
			form_name = form['name']
			try:
				form_list = form_dict[form_name]
				form_list.append(mbid)
				print mbid,form['name'], 'added'
			except:
				form_list = [mbid]
				form_dict[form_name] = form_list
				print mbid,form['name'], 'created'

			#data = form['name']
			#print data 
			#print str(len(data))
			#form_stats = str(len()) + '\t' + form['name'] + '\n'
			#print form_stats
	except:
		print mbid

for form in form_dict:
	print str(len(form_dict[form])) + '\t' + form  + '\n'