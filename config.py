"""

File Organizer Data
Author: Gurpreet Singh
Description: This file contains the popular object extensions with their categorized folder names

"""

EXTENSION_CATEGORY = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
    ".bmp": "Images", ".tiff": "Images", ".webp": "Images",
    ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos", ".mkv": "Videos",
    ".flv": "Videos", ".wmv": "Videos",
    ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio", ".aac": "Audio",
    ".ogg": "Audio", ".m4a": "Audio",
    ".pdf": "Documents", ".txt": "Documents", ".doc": "Documents",
    ".docx": "Documents", ".xls": "Documents", ".xlsx": "Documents",
    ".ppt": "Documents", ".pptx": "Documents",
    ".zip": "Archives", ".rar": "Archives", ".tar": "Archives", ".gz": "Archives",
}

CATEGORY_SYNONYMS = {
    "images": ["images", "pictures", "photos", "pics"],
    "videos": ["videos", "video", "movies", "clips"],
    "audio": ["audio", "music", "songs", "sound"],
    "documents": ["documents", "docs", "files", "text"],
    "archives": ["archives", "zips", "compressed"],
    "others": ["others", "misc", "unsorted", "various"],
}
