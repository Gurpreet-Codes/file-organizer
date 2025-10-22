"""

File Organizer Sorting Code
Author: Gurpreet Singh
Description: This file contains the file processing and sorting functions 
to locate, move, organize, and access a directory.

"""

import shutil
from pathlib import Path
from config import EXTENSION_CATEGORY, CATEGORY_SYNONYMS
import subprocess
import os
import platform


def find_existing_dir(parent: Path, category_name: str):
    """Find an existing folder under parent matching the category (case-insensitive, with synonyms)."""
    candidates = CATEGORY_SYNONYMS.get(category_name.lower(), [category_name.lower()])
    for child in parent.iterdir():
        if child.is_dir():
            name = child.name.lower()
            for cand in candidates:
                if name == cand or cand in name:
                    return child
    return None


def move_file(file_path: Path, dest_folder: Path, log_func):
    """Move a file and log the result."""
    try:
        dest_folder.mkdir(parents=True, exist_ok=True)
        dest_path = dest_folder / file_path.name
        shutil.move(str(file_path), str(dest_path))
        log_func(f"✅ Moved: {file_path.name} → {dest_folder.name}")
    except Exception as e:
        log_func(f"⚠️ Error moving {file_path.name}: {e}")


def organize_files(source_dir, dest_dir, log_func):
    """Organize files by extension into category folders."""
    source = Path(source_dir)
    base = Path(dest_dir) if dest_dir else source

    if not source.exists():
        log_func("⚠️ Source directory not found.")
        return

    count = 0
    for file in source.iterdir():
        if not file.is_file():
            continue

        ext = file.suffix.lower()
        category = EXTENSION_CATEGORY.get(ext, "Others")

        existing = find_existing_dir(base, category)
        dest = existing if existing else base / category

        move_file(file, dest, log_func)
        count += 1
        
    return count


def open_folder_in_explorer(path):
    """Open the folder in the user's default file explorer."""
    try:
        path_str = str(Path(path).resolve())
        system = platform.system()

        if system == "Windows":
            os.startfile(path_str)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", path_str])
        else:  # Linux
            subprocess.run(["xdg-open", path_str])
    except Exception as e:
        print(f"⚠️ Could not open folder: {e}")