import os
import fnmatch
import shutil


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
print fullnames

os.mkdir('Manual_Annotations_Saraga_mp3')
for mp3_files in fullnames:
    shutil.copy2(mp3_files, 'Manual_Annotations_Saraga_mp3')
    
