from pathlib import Path
import shutil
import sys
from folder import document_extensions, image_extensions, program_extensions, audio_extensions, video_extensions, archive_extensions, required_folders, categories

desire = input("\nEnter relative path of the directory (E to Exit): ")

if(desire == "E"):
    print("Program exited successfully\n")
    sys.exit(0)

path = Path(desire)

for folder_name in required_folders:
    folder_name = path / folder_name
    folder_name.mkdir(exist_ok= True)

def get_category(file):
    extension = file.suffix.lower()

    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Other"

def move_file(item, folder):
    shutil.move(item, path / folder)
    filename = str(item).replace(str(path), "")
    print(f"moved {filename} --> {folder}")

for item in path.iterdir():

    if item.is_file():

        category = get_category(item)
        move_file(item, category)

GREEN = "\033[32m"
RESET = "\033[0m"

print(f"{GREEN}\n✓ Sorting completed {RESET}\n")