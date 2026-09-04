# Sift

A lightweight Python utility that automatically organizes files into categorized folders.

## Overview

Sift scans a specified directory, identifies files by their type, and moves them into dedicated folders such as `Documents`, `Images`, `Videos`, `Audio`, `Archives`, and `Programs`.

Files that don't match a defined category are moved into `Other`.

## Features

* Automatically creates required category folders
* Sorts files into categories
* Supports common document, image, program, archive, audio, and video formats
* Handles uppercase and lowercase file extensions
* Moves uncategorized files into `Other`
* Prints each file movement to the console
* Uses Python's built-in filesystem libraries

## Categories

| Category  | Examples                                        |
| --------- | ----------------------------------------------- |
| Documents | `.pdf`, `.docx`, `.txt`, `.csv`, `.pptx`, `.md` |
| Images    | `.jpg`, `.png`, `.gif`, `.webp`, `.svg`         |
| Programs  | `.exe`, `.msi`, `.bat`, `.cmd`, `.msix`         |
| Archives  | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.iso`    |
| Audio     | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`         |
| Videos    | `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`         |
| Other     | Files that don't match a defined category       |

## How It Works

Sift uses `pathlib` to inspect the target directory and `shutil` to move files.

The program:

1. Creates the required category folders if they don't exist.
2. Scans the target directory.
3. Checks each item to determine whether it is a file.
4. Determines the file type.
5. Moves the file into the appropriate category.
6. Places unsupported file types into `Other`.

## Project Structure

```text
sift/
├── main.py
├── folder.py
└── README.md
```

### `main.py`

Contains the sorting logic, directory handling, and file-moving functionality.

### `folder.py`

Contains the file extension lists used to determine how files are categorized.

## Requirements

* Python 3.x
* No external Python packages required

Sift uses standard Python libraries:

```python
pathlib
shutil
```

## Configuration

The directory being organized can be changed in `main.py`:

```python
path = Path("../../Downloads")
```

File categories can be customized by modifying the extension lists in `folder.py`.

## Usage

Clone the repository and run:

```bash
python main.py
```

Make sure the configured directory exists and contains files you want to organize.

> **Note:** Test Sift on a copy of a directory before using it on important files.

## Roadmap

* [ ] Replace extension checks with a category mapping
* [ ] Add error handling for failed file operations
* [ ] Add duplicate-file handling
* [ ] Add logging
* [ ] Make categories configurable
* [ ] Add directory watching
* [ ] Run automatically in the background

## Developer

Under development by `alloy01`
