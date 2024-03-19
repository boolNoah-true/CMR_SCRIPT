import shutil
import os

#Function to copy and rename a folder
def copy_and_rename(source, destination, new_name):
    #Create the new folder path with the new folder name
    new_folder_path = os.path.join(destination, new_name)
    #Copy the folder
    shutil.copytree(source, new_folder_path)
    print(f"Folder copied from {source} to {new_folder_path}")
#function for counting number of folders in directory
index = 0
def count_folders(directory):
    global index

    folder_count = len([name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))])
    
    index = folder_count + 1



source_folder = "E:\CIS 17B ASSIGNMENTS\Shopping Catalog"
destination_folder = "E:\FROST Versions"

count_folders(destination_folder)

new_name = f"FROST_Version_{index}"

copy_and_rename(source_folder, destination_folder, new_name)
