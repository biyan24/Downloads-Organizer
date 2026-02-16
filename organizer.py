import os
import shutil

download_path = os.path.expanduser("~/Downloads")

folders = {
    "Documents": ["doc", "docx", "pdf", "txt"],
    "Images": ["jpg", "jpeg", "png", "gif", "svg"],
    "Videos": ["mp4", "avi", "mkv", "mov"],
    "Music": ["mp3", "wav", "flac", "aac"],
    "Archives": ["zip", "rar", "tar", "gz", "xz"],
    "Executables": ["exe", "bat", "sh", "appimage"],
}

confirm = input("Organize Downloads? (y/n): ")
if confirm.lower() != "y":
    exit()

for filename in os.listdir(download_path):
    file_path = os.path.join(download_path, filename)

    if os.path.isdir(file_path):
        continue

    ext = filename.split(".")[-1].lower()

    for folder_name, extensions in folders.items():
        if ext in extensions:
            target_folder = os.path.join(download_path, folder_name)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} to {folder_name}")
            break

print("Processing Completed")
