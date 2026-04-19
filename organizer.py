import os
import shutil
import time
class FileOrganizer:
    def __init__(self, path):
        self.path = path
    def scan(self):
        return os.listdir(self.path)
    def get_type(self, file):
        ext = os.path.splitext(file)[1].lower()
        if ext in [".jpg", ".png", ".jpeg"]:
            return "Images"
        elif ext in [".pdf", ".txt", ".docx"]:
            return "Documents"
        elif ext in [".mp4", ".mkv"]:
            return "Videos"
        else:
            return "Others"
    def move(self, file):
        source = os.path.join(self.path, file)
        folder = self.get_type(file)
        target_folder = os.path.join(self.path, folder)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        destination = os.path.join(target_folder, file)
        shutil.move(source, destination)
        print(f"Moved: {file} -> {folder}")
    def start(self):
        print("Automation started...")
        while True:
            files = self.scan()
            for file in files:
                file_path = os.path.join(self.path, file)
                if os.path.isfile(file_path):
                    self.move(file)

            time.sleep(5)
