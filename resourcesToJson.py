import os
import tkinter as tk
from tkinter import filedialog
import json


def extract_file_info(root_dir):
    resources = {}
    ignored_files = [".gitattributes", "license", "readme.md"]
    resource_id = 1  # init resource_id outside the loop

    for category in os.listdir(root_dir):
        if category == ".git":
            continue  # skip  .git directory

        category_path = os.path.join(root_dir, category)

        if not os.path.isdir(category_path):
            continue

        category_resources = []

        for filename in os.listdir(category_path):
            if filename.lower() in ignored_files:
                continue

            if os.path.isfile(os.path.join(category_path, filename)):
                name_without_extension = os.path.splitext(filename)[0]
                file_extension = os.path.splitext(filename)[1].lstrip(
                    "."
                )
                parts = name_without_extension.split("__")
                title = parts[0]
                credit = parts[1] if len(parts) > 1 else ""

                title = " ".join(word.capitalize() for word in title.split())

                resource = {
                    "id": resource_id,
                    "title": title,
                    "credit": credit,
                    "filetype": file_extension,
                }
                category_resources.append(resource)
                resource_id += 1

        resources[category] = category_resources

    return resources


def write_resources_to_file(resources, output_file="resources.json"):
    with open(output_file, "w") as f:
        json.dump(resources, f, indent=2)


def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()
    return folder_selected


def main():
    directory = select_directory()

    if directory:
        resources = extract_file_info(directory)
        write_resources_to_file(resources)
        print("resources.json file created successfully.")
    else:
        print("No directory selected.")


if __name__ == "__main__":
    main()
