from pathlib import Path
import shutil
from folder import document_extensions, image_extensions, program_extensions, audio_extensions, video_extensions, archive_extensions

path = Path("../../Downloads")

required_folders = [
    "Documents",
    "Images",
    "Programs",
    "Other",
    "Videos",
    "Audio",
    "Archives",
]

for folder_name in required_folders:
    folder_name = path / folder_name
    folder_name.mkdir(exist_ok= True)

def move_file(item, folder):
    shutil.move(item, path / folder)
    filename = str(item).replace(str(path), "")
    print(f"moved {filename} --> {folder}")

for item in path.iterdir():

    if item.is_file():

        extension = item.suffix.lower()
        
        if extension in document_extensions:
            move_file(item, "Documents")
        elif extension in image_extensions:
            move_file(item, "Images")
        elif extension in program_extensions:
            move_file(item, "Programs")
        elif extension in archive_extensions:
            move_file(item, "Archives")
        elif extension in video_extensions:
            move_file(item, "Videos")
        elif extension in audio_extensions:
            move_file(item, "Audio")
        else:
            move_file(item, "Other")

GREEN = "\033[32m"
RESET = "\033[0m"

print(f"{GREEN}\n✓ Sorting completed {RESET}")