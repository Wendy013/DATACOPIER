import os
import shutil

def copy_folder(entrance, output):
    files_img = []

    for root, dirs, files in os.walk(entrance):
        for file in files:
            files_img.append(os.path.join(root, file))

    for file in files_img:
        name = os.path.basename(file)
        folder = name.split(".")[0]
        os.makedirs(os.path.join(output, folder), exist_ok=True)
        shutil.copy(file, os.path.join(output, folder, name))















