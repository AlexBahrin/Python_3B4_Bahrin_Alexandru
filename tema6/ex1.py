import os
import sys

try:
    if len(sys.argv) != 3:
        raise ValueError("Usage: python script.py <directory_path> <file_extension>")

    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.isdir(directory):
        raise FileNotFoundError("Invalid directory path.")

    if not extension.startswith("."):
        raise ValueError("File extension must start with a '.'")

    found = False
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                found = True
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        print(f"\n--- Contents of {file_path} ---")
                        print(f.read())
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    if not found:
        print("No files found with the given extension.")

except Exception as e:
    print("Error:", e)