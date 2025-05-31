# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

from .scripts.revisit_selection_files import revisit_selection_files

# drive = None

# def get_drive():
#     gauth = GoogleAuth()
#     gauth.LocalWebserverAuth()

#     global drive
#     if not drive:
#         drive = GoogleDrive(gauth)
#     return drive

img_list = []

root_selection_folder = "C:/Projects/Photo-Selector/photo_selector/selection_files"


def get_unvisited_imgs():
    global img_list
    if not img_list:
        print(" --- Fetching unvisited file --- ")
        with open(root_selection_folder+"/unvisited.txt", 'r') as file:
            img_list = [line.strip() for line in file.readlines()]

    if len(img_list) == 1:
        revisit_selection_files()
    return img_list


def photo():
    images = get_unvisited_imgs()
    return images.pop()


def unvisited_photos_count():
    return len(img_list)
