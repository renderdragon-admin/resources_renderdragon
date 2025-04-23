import os
import tkinter as tk
from tkinter import filedialog
import shutil


def convert_to_lowercase(root_dir):

    ignored_items = [".git", ".gitattributes", "license", "readme.md", "lowerall.py", "resourcesToJson.py"]

    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)

        if item.lower() in ignored_items:
            continue

        if os.path.isfile(item_path):
            new_name = item.lower()
            new_path = os.path.join(root_dir, new_name)
            try:
                os.rename(item_path, new_path)
            except FileExistsError:
                print(
                    f"Skipping rename of {item} due to existing file with"
                    " lowercase name."
                )
        elif os.path.isdir(item_path):
            convert_to_lowercase(item_path)
            new_name = item.lower()
            new_path = os.path.join(root_dir, new_name)
            try:
                os.rename(item_path, new_path)
            except FileExistsError:
                print(
                    f"Skipping rename of {item} due to existing directory"
                    " with lowercase name."
                )
            except OSError as e:
                print(f"Error renaming directory {item}: {e}")


def select_directory():
    root = tk.Tk()
    root.withdraw()  # hide  main window
    folder_selected = filedialog.askdirectory()
    return folder_selected


def main():
    directory = select_directory()

    if directory:
        convert_to_lowercase(directory)
        print(f"All files in {directory} converted to lowercase (except"
              " ignored items).")
    else:
        print("No directory selected.")


if __name__ == "__main__":
    main()
