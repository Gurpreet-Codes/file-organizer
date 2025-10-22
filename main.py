"""

File Organizer GUI
Author: Gurpreet Singh
Description: Sorts files by type (Images, Videos, Audio, Documents, etc.). Easy to use and modify.
GUI built with CustomTkinter.

"""


import os
import platform
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path
import threading
from file_sorter import organize_files, open_folder_in_explorer


# --------------- ICON & RESOURCE HANDLING ---------------

class FileOrganizerApp(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("📁 File Organizer")
        self.geometry("750x550")
        ctk.set_appearance_mode("system")  # or "dark" / "light"
        ctk.set_default_color_theme("blue")

        # --- Variables ---
        self.source_dir = ctk.StringVar()
        self.dest_dir = ctk.StringVar()
        self.total_files = 0

        # --- Layout ---
        self.create_widgets()

        icon_path = Path("assets/icon.ico")
        if icon_path.exists():
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

    # GUI Layout

    def create_widgets(self):
        
        title_label = ctk.CTkLabel(
            self, text="📁 File Organizer",
            font=("Segoe UI", 26, "bold")
        )
        title_label.pack(pady=(20, 10))

        # Frame for folder selections
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=10, fill="x")

        # Source folder
        ctk.CTkLabel(frame, text="Source Folder:").grid(
            row=0, column=0, sticky="w", padx=10, pady=10)
        ctk.CTkEntry(frame, textvariable=self.source_dir, width=420).grid(
            row=0, column=1, padx=10)
        ctk.CTkButton(frame, text="Browse", command=self.select_source).grid(
            row=0, column=2, padx=10)

        # Destination folder
        ctk.CTkLabel(frame, text="Destination Folder:").grid(
            row=1, column=0, sticky="w", padx=10, pady=10)
        ctk.CTkEntry(frame, textvariable=self.dest_dir, width=420).grid(
            row=1, column=1, padx=10)
        ctk.CTkButton(frame, text="Browse", command=self.select_dest).grid(
            row=1, column=2, padx=10)

        # Buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=15)
        ctk.CTkButton(
            btn_frame, text="🧹 Organize Files",
            command=self.start_organize_thread, width=200, height=40
        ).pack(side="left", padx=15)
        ctk.CTkButton(
            btn_frame, text="🗑 Clear Log",
            command=self.clear_log, width=150
        ).pack(side="left", padx=15)

        # Progress bar
        self.progress_var = ctk.DoubleVar()
        self.progress_bar = ctk.CTkProgressBar(self, variable=self.progress_var)
        self.progress_bar.pack(fill="x", padx=40, pady=(5, 10))
        self.progress_bar.set(0)

        # Log
        ctk.CTkLabel(self, text="Activity Log:").pack(anchor="w", padx=25)
        self.log_box = ctk.CTkTextbox(self, width=700, height=250)
        self.log_box.pack(padx=25, pady=(5, 10))

        # Status bar
        self.status_label = ctk.CTkLabel(self, text="Ready.", anchor="w")
        self.status_label.pack(fill="x", padx=20, pady=(0, 10))

    # Helpers

    def log(self, text):
        self.log_box.insert("end", text + "\n")
        self.log_box.see("end")
        self.update()

    def clear_log(self):
        self.log_box.delete("1.0", "end")
        self.progress_var.set(0)
        self.status_label.configure(text="Ready.")

    def select_source(self):
        folder = filedialog.askdirectory(
            title="Select Source Folder", initialdir=self.get_default_folder())
        if folder:
            self.source_dir.set(folder)

    def select_dest(self):
        folder = filedialog.askdirectory(
            title="Select Destination Folder", initialdir=self.get_default_folder())
        if folder:
            self.dest_dir.set(folder)

    def get_default_folder(self):
        system = platform.system()
        if system == "Windows":
            return os.path.join(os.environ["USERPROFILE"], "Downloads")
        elif system == "Darwin":
            return str(Path.home() / "Downloads")
        else:
            return str(Path.home())
    

    # Main actions

    def start_organize_thread(self):
        """Run organize in a separate thread (so UI doesn't freeze)."""
        thread = threading.Thread(target=self.start_organize)
        thread.start()

    def start_organize(self):
        src = self.source_dir.get().strip()
        dest = self.dest_dir.get().strip() or None

        if not src:
            messagebox.showerror("Error", "Please select a source folder.")
            return

        self.clear_log()
        self.log(f"🔍 Source: {src}")
        self.log(f"📦 Destination: {dest or src}\n")

        # Count total files first
        files = [f for f in Path(src).iterdir() if f.is_file()]
        self.total_files = len(files)

        if self.total_files == 0:
            self.log("⚠️ No files found in the selected directory.")
            self.status_label.configure(text="No files to organize.")
            return

        # Start organization
        self.status_label.configure(text="Organizing files...")
        self.update_idletasks()

        sorted_count = organize_files(src, dest, self.log) or 0

        # Update status
        self.status_label.configure(text=f"✨ Done! Sorted {sorted_count} files.")
        self.log(f"\n✅ Completed! {sorted_count} files organized successfully.\n")

        # Automatically open the destination folder
        target = dest or src
        self.log(f"📂 Opening folder: {target}")
        open_folder_in_explorer(target)


        def progress_logger(message):
            self.log(message)
            moved = self.log_box.get("1.0", "end").count("✅ Moved")
            progress = moved / max(self.total_files, 1)
            self.progress_var.set(progress)
            self.status_label.configure(
                text=f"Progress: {int(progress * 100)}% ({moved}/{self.total_files})")

        organize_files(src, dest, progress_logger)

        self.status_label.configure(text="✨ Done! Files organized.")
        self.progress_var.set(1.0)
        self.log("✅ All files processed.\n")


if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()
