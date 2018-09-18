import os


hasfolder = False
folder_path = ''

while hasfolder == False:
    folder_path = input('Insert full folder path to arrange: ')
    warning = input(f'Is this the folder you want to arrange "{folder_path}"? [y/n then ENTER] ')
    if 'y' in warning or 'Y' in warning:
        hasfolder = True
        os.chdir(folder_path)

sound_types = ['m4a', 'mp3']
image_types = ['jpg', 'png']
video_types = ['mov', 'mp4', 'mkv', 'mpg']

def is_file_type(file_types, filename):
    for file_type in file_types:
        if '.'+file_type in filename:
            return True
    return False

def create_folder(folder):
    try:
        os.mkdir(folder_path+'/'+folder)
    except FileExistsError:
        pass

def move_file_to(file_name, folder):
    create_folder(folder)
    os.rename(file_name, folder+'/'+file_name)
    print(f'moved file {file_name} to {folder}')

# Arrange filenames by type
for r, d, files in os.walk('.'):
    for file in files:
        # Ignore some files
        if file[0] == '.':
            continue
        if is_file_type(sound_types, file):
            move_file_to(file, 'sounds')
        elif is_file_type(image_types, file):
            move_file_to(file, 'images')
        elif is_file_type(video_types, file):
            move_file_to(file, 'videos')
        elif is_file_type(['pdf'], file):
            move_file_to(file, 'pdf')
        else:
            move_file_to(file, 'other')
