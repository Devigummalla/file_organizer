import os
import shutil
import time
from plyer import notification

# Set your downloads folder path
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), r"C:\Users\JHANSI GUMMALLA\Desktop\sample")

# File type mappings
FILE_TYPES = {
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Installers": [".exe", ".msi", ".dmg", ".apk"],
    "Scripts": [".py", ".js", ".html", ".css", ".php"],
    "Others": []
}

def move_file(file_path, dest_folder):
    """Moves a file to the destination folder, creating the folder if needed."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        shutil.move(file_path, dest_folder)
        return True
    except Exception as e:
        print(f"Error moving {file_path}: {e}")
        return False

def organize_files():
    """Organizes files in the downloads folder into categorized subfolders."""
    moved_files = []

    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest_folder = os.path.join(DOWNLOADS_FOLDER, category)
                    if move_file(file_path, dest_folder):
                        moved_files.append((filename, category))
                    moved = True
                    break

            if not moved:
                dest_folder = os.path.join(DOWNLOADS_FOLDER, "Others")
                if move_file(file_path, dest_folder):
                    moved_files.append((filename, "Others"))

    if moved_files:
        notify_user(len(moved_files))

def notify_user(file_count):
    """Send desktop notification about moved files."""
    notification.notify(
        title="🗂 File Organizer",
        message=f"{file_count} file(s) organized in Downloads folder!",
        timeout=5
    )

if __name__ == "__main__":
    print("🛠 Organizing files...")
    organize_files()
    print("✅ Done!")
