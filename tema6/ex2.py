import os
import sys

try:
    if len(sys.argv) != 2:
        raise ValueError("Usage: python script.py <directory_path>")

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        raise FileNotFoundError("The specified directory does not exist.")

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        print("No files found in the directory.")
        sys.exit()

    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(directory, filename)
        name, ext = os.path.splitext(filename)
        new_filename = f"file{i}{ext}"
        new_path = os.path.join(directory, new_filename)
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

except Exception as e:
    print("Error:", e)