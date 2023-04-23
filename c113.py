import os
import shutil
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "/Users/abhijoy/Downloads"
destination = "/Users/abhijoy/Desktop"

dir_tree = {"Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif', ".JPEG"],
            "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
            "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], 
            "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name, extention = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extention in value:
                file_name = os.path.basename(event.src_path)
                path1 = source + "/" + file_name 
                path2 = destination + "/" + key 
                path3 = destination + "/" + key + "/" + file_name

                if os.path.exists(path2):
                    print("Directory Exists")
                    print("Moving")
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    print("Making Directory")
                    os.makedirs(path2)
                    print("Moving")
                    shutil.move(path1, path3)
                    time.sleep(1)

    def on_deleted(self, event):
        print(f"{event.src_path} was moved")
        
        
    def on_moved(self, event):
       print(f"{event.src_path} was moved")
    
    def on_modified(self, event):
        print(f"{event.src_path} was moved")
        
    
event_handler = FileMovementHandler()

observer = Observer()
observer.schedule(event_handler, source, recursive = True)
observer.start()

try:
    while(True):
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()

