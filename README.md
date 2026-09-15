# Filtr

A lightweight Python CLI utility that automatically organizes files into categorized folders.

## Overview

filtr scans a specified directory, identifies files by their extensions, and moves them into dedicated folders such as `Documents`, `Images`, `Videos`, `Audio`, `Archives`, and `Programs`.

Files that don't match a defined category are moved into `Other`.

filtr can also perform a **dry run**, allowing you to preview what would be moved without actually changing any files.

## Features

* Automatically creates required category folders
* Sorts files based on their extensions
* Supports common document, image, program, archive, audio, and video formats
* Handles uppercase and lowercase file extensions
* Moves uncategorized files into `Other`
* Supports command-line arguments using `argparse`
* Supports `--dry-run` mode
* Prints each file movement to the console
* Uses only Python's standard library

## Categories

| Category  | Examples                                                         |
| --------- | ---------------------------------------------------------------- |
| Documents | `.pdf`, `.docx`, `.txt`, `.csv`, `.pptx`, `.md`                  |
| Images    | `.jpg`, `.png`, `.gif`, `.webp`, `.svg`, `.ico`                  |
| Programs  | `.exe`, `.msi`, `.bat`, `.cmd`, `.com`, `.scr`, `.msix`          |
| Archives  | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`, `.iso`      |
| Audio     | `.mp3`, `.wav`, `.flac`, `.aac`, `.m4a`, `.ogg`, `.opus`, `.wma` |
| Videos    | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`, `.m4v`  |
| Other     | Files that don't match a defined category                        |

## How It Works

filtr uses `pathlib` to inspect directories and `shutil` to move files.

The program:

1. Receives the target directory through a command-line argument.
2. Creates the required category folders if they don't exist.
3. Scans the target directory.
4. Checks whether each item is a file.
5. Determines its category from its file extension.
6. Moves the file into the appropriate category.
7. Places unsupported file types into `Other`.

When `--dry-run` is enabled, filtr performs all classification and displays the planned movements without moving the files.

## Project Structure

```text
filtr/
├── main.py
├── folder.py
└── README.md
```

### `main.py`

Contains the CLI interface, directory handling, file classification, and file-moving logic.

### `folder.py`

Contains the category definitions and supported file extensions.

## Requirements

* Python 3.x
* No external Python packages required

filtr uses Python's standard library:

```python
pathlib
shutil
argparse
```

## Usage

### Basic Usage

Run filtr by providing the directory you want to organize:

```bash
python3 main.py <path>
```

Example:

```bash
python3 main.py ~/Downloads
```

### Dry Run

Use `--dry-run` to preview the changes without moving any files:

```bash
python3 main.py ~/Downloads --dry-run
```

Short form:

```bash
python3 main.py ~/Downloads -d
```

Example output:

```text
moved /image.png --> Images
moved /report.pdf --> Documents
moved /song.mp3 --> Audio

✓ Sorting completed
```

In dry-run mode, these movements are only displayed and no files are moved.

## Command-Line Arguments

| Argument          | Description                                 |
| ----------------- | ------------------------------------------- |
| `path`            | Directory that filtr should organize         |
| `-d`, `--dry-run` | Preview file movements without moving files |

You can also view the available options with:

```bash
python3 main.py --help
```

## Configuration

File categories and supported extensions can be customized in `folder.py`.

For example:

```python
categories = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png"],
}
```

Any extension that isn't found in the category mapping is automatically assigned to `Other`.

## Safety

filtr moves files rather than copying them.

Before using filtr on important files, it is recommended to:

* Test it with `--dry-run`
* Test it on a temporary directory
* Keep backups of important data

## Developer

Developed by `alloy01`.
