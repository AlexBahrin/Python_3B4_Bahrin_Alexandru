import os
import sys

try:
    if len(sys.argv) != 2:
        raise ValueError("Usage: python script.py <directory_path>")

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        raise FileNotFoundError("The specified directory does not exist.")

    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                total_size += os.path.getsize(file_path)
            except PermissionError:
                print(f"Permission denied: {file_path}")
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            except Exception as e:
                print(f"Error accessing {file_path}: {e}")

    print(f"Total size of all files: {total_size} bytes")

except Exception as e:
    print("Error:", e)