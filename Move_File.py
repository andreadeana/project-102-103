import os
import shutil


from_dir = "C:/Users/admin/Downloads"
to_dir = "C:/Users/admin/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                       
        path2 = to_dir + '/' + "Document_Files"                           
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name 

if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)
else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)













# import sys
# import time
# import random
# import os
# import shutil
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler