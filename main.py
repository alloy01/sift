from pathlib import Path
import shutil
from folder import required_folders, categories
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("path", type=str, help="enter the relative path of the directory that needs to be sorted")
parser.add_argument("-d", "--dry_run", action="store_true", help="preview changes without moving files")

args = parser.parse_args()

path = Path(args.path)

GREEN = "\033[32m"
RESET = "\033[0m"

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
    if not args.dry_run:
        shutil.move(item, path / folder)
    filename = str(item).replace(str(path), "")
    print(f"{GREEN}moved{RESET} {filename} --> {folder}")

for item in path.iterdir():

    if item.is_file():

        category = get_category(item)
        move_file(item, category)

print(f"{GREEN}\n✓ Sorting completed {RESET}\n")