#!/usr/local/opt/python/bin/python3.6

# -*- coding: utf-8 -*-
import os
import sys
import shutil

if len(sys.argv) < 2:
    print('No path given')
    sys.exit()

try:
    os.chdir(sys.argv[1])
except FileNotFoundError:
    print('No such file or directory')
    sys.exit()

sound_types = ['m4a', 'mp3']
image_types = ['jpg', 'png']
video_types = ['mov', 'mp4', 'mkv', 'mpg']

final_folders = ('videos', 'sounds', 'images', 'pdf', 'other')

def is_file_type(file_types, filename):
    for file_type in file_types:
        if '.'+file_type in filename:
            return True
    return False

def create_folder(folder):
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass

def move_file_to(file_path, folder):
    create_folder(folder)
    try:
        file = file_path.split('/')[-1]
        os.rename(file_path, folder+'/'+file)
        print(f'moved file {file_path} to {folder}')
    except FileNotFoundError:
        pass # File already on folder

# Arrange filenames by type
for r, d, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(r, file)
        # Ignore (dot) files and files already on the final folder
        if file[0] == '.' or r[2:] in final_folders:
            continue
        if is_file_type(sound_types, file):
            move_file_to(file_path, 'sounds')
        elif is_file_type(image_types, file):
            move_file_to(file_path, 'images')
        elif is_file_type(video_types, file):
            move_file_to(file_path, 'videos')
        elif is_file_type(['pdf'], file):
            move_file_to(file_path, 'pdf')
        else:
            move_file_to(file, 'other')

# Remove empty folders
for p, dirs, f in os.walk('.'):
    for d in dirs:
        if d not in final_folders:
            shutil.rmtree(d)
