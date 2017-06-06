#to get the manual annotations
#go to pycompmusic 
#import pickle
import os
import compmusic
from compmusic import dunya

dunya.set_token("67a11dc1e00e22cb4bc387ee870129a819989212")

#compmusic.dunya.docserver.get_collections()
collection = compmusic.dunya.docserver.get_collection('dunya-carnatic-cc')

#compmusic.dunya.docserver.file_for_document(recordingid, thetype, subtype=None, part=None, version=None)
#recording id = MBID 
#type = the computed filetype

os.makedirs("Manual_Annotations")
for document in collection['documents']:
	mbid =  document['external_identifier']
	print mbid 
	source_list = compmusic.dunya.docserver.document(mbid)['sourcefiles']
	mbid_path = 'Manual_Annotations' + '/' + mbid
	os.makedirs(mbid_path)
	for source in source_list:
		annotation =  compmusic.dunya.docserver.file_for_document(mbid, source)
		print source
		file_name = mbid_path + '/' + source + '.txt'
		file = open(file_name,'w')
		file.write(annotation)
		#pickle.dump(annotation, file)
		file.close


'''
mbid =  collection['documents'][0]['external_identifier']
source_list = compmusic.dunya.docserver.document(mbid)['sourcefiles']

print source_list[0]
annotation =  compmusic.dunya.docserver.file_for_document(mbid, source_list[0])

print annotation

file = open('manual_annotation.txt','w')
#pickle.dump(annotation, file)
file.write(annotation)
file.close()
'''