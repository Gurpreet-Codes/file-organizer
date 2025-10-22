File Organizer – Smart Desktop File Management System created by Gurpreet Singh (myself)!!

File Organizer is a smart and user-friendly desktop tool that automatically sorts and organizes your files into categorized folders like Images, Videos, Documents, Audio, Archives, and Others.

It features a modern GUI built with CustomTkinter, designed for simplicity and ease of use — no terminal knowledge required!

Features:

✅ Beautiful Interface – Modern, clean, and dark-mode–friendly GUI.
🧠 Automatic Sorting – Detects file types and categorizes them intelligently.
📁 Smart Folder Detection – Recognizes pre-existing folders (e.g. images, photos) regardless of case.
🗂 Custom Destination Support – Choose where to send your files or sort them in place.
🪟 Cross-Platform Compatibility – Works seamlessly on Windows, macOS, and Linux.
📂 Auto Open Folder – Automatically opens the destination folder after organizing.
💾 One-Click Packaging – Easily turn into a .exe or .app using PyInstaller.

🧩 Tech Stack

Python 3.10+

CustomTkinter – GUI framework

Pathlib & Shutil – File and directory handling

PyInstaller – Packaging tool for standalone executables

🚀 Installation & Usage
🪄 Option 1: Run from Source

Clone the repository:

git clone https://github.com/Gurpreet-Codes/file-organizer
cd file-organizer


Install dependencies:

pip install customtkinter


Run the app:

python main.py

💾 Option 2: Run as Executable (Windows/macOS)

Download the latest .exe or .app from the Releases
 section.

Double-click to launch — no Python setup required!

🖼️ Screenshots
Before Sorting	After Sorting

	
⚙️ How It Works

Select a source folder containing your unsorted files.

(Optional) Choose a destination folder — or leave it blank to sort in place.

Click Organize Files.

The program will:

Identify file extensions

Move files into category folders

Skip folders and invalid files

Open the sorted folder automatically

🧠 File Categories
Category	Extensions
Images	.jpg, .jpeg, .png, .gif, .bmp, .webp, .tiff
Videos	.mp4, .mov, .avi, .mkv, .flv, .wmv
Audio	.mp3, .wav, .flac, .aac, .ogg, .m4a
Documents	.pdf, .docx, .txt, .xlsx, .pptx
Archives	.zip, .rar, .tar, .gz
Others	Everything else
🧱 Project Structure
file-organizer/
│
├── main.py              # GUI application entry point
├── file_sorter.py           # Core sorting and helper functions
├── config.py            # Extension and folder data
├── requirements.txt     # Dependencies
└── README.md            # This file

👨‍💻 Contributing

Contributions are welcome!
If you have ideas for improvements or bug fixes:

Fork the repo

Create your feature branch (git checkout -b feature/new-feature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/new-feature)

Open a Pull Request

🪪 License

This project is licensed under the MIT License – free for personal and commercial use.

💬 Support

If you enjoy this project, please ⭐ star the repo and share it!
For issues or feature requests, open a ticket in the Issues section.

Made with ❤️ in Python