import os
import sys
from collections import defaultdict

try:
    if len(sys.argv) != 2:
        raise ValueError("Usage: python script.py <directory_path>")

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        raise FileNotFoundError("The specified directory does not exist.")

    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except PermissionError:
        raise PermissionError("Permission denied: unable to access directory.")

    if not files:
        print("The directory is empty.")
        sys.exit()

    extension_counts = defaultdict(int)

    for file in files:
        _, ext = os.path.splitext(file)
        ext = ext.lower() if ext else "no_extension"
        extension_counts[ext] += 1

    print("File counts by extension:")
    for ext, count in extension_counts.items():
        print(f"{ext}: {count}")

except Exception as e:
    print("Error:", e)