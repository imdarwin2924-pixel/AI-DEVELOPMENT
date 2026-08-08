from tools.file_tools import scan_directory

folder = "data/sample_folder"

files = scan_directory(folder)

print(f"Found {len(files)} files:\n")

for file in files:
    print(file)