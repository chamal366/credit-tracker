import os
import shutil

path = input("Enter the path of the folder you want to organize: ")
files = os.listdir(path)       
for file in files:
    filename, file_extension = os.path.splitext(file)
    extension = file_extension[1:] # Remove the dot from the extension

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
