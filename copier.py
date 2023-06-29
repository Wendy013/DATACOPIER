import os
import shutil

class copy_files:
    def filecopier(files, output):
        for file in files:
            name = os.path.basename(file)
            folder = name.split(".")[0]
            os.makedirs(os.path.join(output,folder), exist_ok=True)
            shutil.copy(file, os.path.join(output,folder,name))















