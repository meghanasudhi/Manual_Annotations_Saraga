import musicbrainzngs
import os
import fnmatch
import shutil
import csv


def get_filenames_in_dir(dir_name, keyword='*.mp3', skip_foldername='',
                         match_case=True, verbose=None):
    names = []
    folders = []
    fullnames = []

    if verbose:
        print(dir_name)

    # check if the folder exists
    if not os.path.isdir(dir_name):
        if verbose:
            print("> Directory doesn't exist!")
        return [], [], []

    # if the dir_name finishes with the file separator,
    # remove it so os.walk works properly
    dir_name = dir_name[:-1] if dir_name[-1] == os.sep else dir_name

    # walk all the subdirectories
    for (path, dirs, files) in os.walk(dir_name):
        for f in files:
            has_key = (fnmatch.fnmatch(f, keyword) if match_case else
                       fnmatch.fnmatch(f.lower(), keyword.lower()))
            if has_key and skip_foldername not in path.split(os.sep)[1:]:
                try:
                    folders.append(str(path))
                except TypeError:  # already unicode
                    folders.append(path)
                try:
                    names.append(str(f))
                except TypeError:  # already unicode
                    names.append(path)
                fullnames.append(os.path.join(path, f))

    if verbose:
        print("> Found " + str(len(names)) + " files.")
    return fullnames, folders, names

fullnames, folders, names = get_filenames_in_dir(dir_name='/Users/meghanasudhindra/Manual_Annotations_Saraga')
mbid_list = []
for path in names:
	MBID_name = os.path.splitext(os.path.basename(path))[0]
	mbid_list.append(MBID_name)
	print MBID_name


musicbrainzngs.auth("meghanasudhindra", "musicbrains123")

musicbrainzngs.set_useragent("Dunya", "0.1")
musicbrainzngs.set_hostname("beta.musicbrainz.org")

MBID_Song = open("MBID_Song.txt", "w")
#recordings = []
recording_id = []
recording_title = []
#artist_id = "4cc5200e-a3f7-4d5d-8b15-9b10a8f9a9a2"
for name_artist in mbid_list:
    result = musicbrainzngs.get_recording_by_id(name_artist)
    print result['recording']['id']
    print result['recording']['title']
    recording_id.append(result['recording']['id'])
    recording_title.append(result['recording']['title'])

for i in range(len(recording_id)):
    MBID_Song.write(recording_id[i] + '\t' + recording_title[i] + '\n')
MBID_Song.close()






