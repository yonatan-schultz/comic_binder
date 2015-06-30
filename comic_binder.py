#!/usr/bin/env python

#must have pyunpack installed "pip install pyunpack"
#must have patool installed "pip install patool"

# Welcome to Comic Binder! It is a simple Python script that zips up multiple cbr and cbz files into a single zip file readable by PerfectViewer or other comic readers. 
# It is useful for finished series or mini-series that you've collected in individual issues and would like to roll up into a single file.
# For now, simply drop it into the folder that contains the comic files and let it run. It will:
# 1. Extract all files
# 2. Zip them together into a cbz file
# 3. Delete all individual cbr and cbz files
# 
# When it's done you'll be left with a single .cbz file named after the folder that you are currently in. It expects a file structure of:
#
#
# My Comic Collection
# --------Series 1
# -------------Issue 1
# -------------Issue 2
# -------------Issue 3
# --------Series 2
# -------------Issue 1
# -------------Issue 2
# -------------Issue 3

import os.path
from os import walk
from pyunpack import Archive
import zipfile
import shutil

#create a directory named after our currect directory 
directory = os.getcwd().split('/')[-1]
os.mkdir(directory)

#find all the files in the current directory
f = []
for dirpath, dirnames, filenames in os.walk("."):
    f.extend(filenames)
    break

#now make an array that just includes the cbr and cbz files
suffix = ['.cbr','.cbz']
comics = [comic for comic in filenames if os.path.splitext(comic)[1] in suffix]

#fuckin' extract it all.
for comic in comics:
	Archive(comic).extractall(directory)

#delete the group jpg

#for dirpath, dirnames, filenames in os.walk(directory):
#	os.remove(os.path.join(dirpath,filenames[-1]))

#make a zipfile out of the extracted files
zf = zipfile.ZipFile(directory + ".zip", "w")
for dirname, subdirs, files in os.walk(directory):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()

#now let's do some cleanup
shutil.rmtree(directory)
os.rename(directory + ".zip",directory + ".cbz")

#fuckin' delete it all
for comic in comics:
	os.remove(comic)

