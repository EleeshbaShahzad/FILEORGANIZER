import os
import shutil
from config import FILE_TYPES


class FileOrganizer:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def create_folders(self):
        for folder in FILE_TYPES.keys():
            path = os.path.join(self.folder_path, folder)
            if not os.path.exists(path):
                os.makedirs(path)

    def organize(self):
        files = os.listdir(self.folder_path)

        for file in files:
            file_path = os.path.join(self.folder_path, file)

            if os.path.isfile(file_path):
                self.move_file(file)

    def move_file(self, file):
        file_path = os.path.join(self.folder_path, file)
        extension = os.path.splitext(file)[1]

        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                destination = os.path.join(self.folder_path, folder, file)
                shutil.move(file_path, destination)
                break