import os
import shutil

source = input("Enter the Source Folder :")
destination = input("Enter the Destination Folder :")

source = source + "/"
destination = destination + "/"

listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file) , destination)
