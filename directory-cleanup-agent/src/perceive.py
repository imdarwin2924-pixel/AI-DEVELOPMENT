from tools.file_tools import scan_directory


def perceive(folder_path):
    """
    Perceive Stage:
    Scan the target directory and return file information.
    """

    print("\n========== PERCEIVE STAGE ==========")
    print(f"Scanning folder: {folder_path}")

    files = scan_directory(folder_path)

    print(f"\nFound {len(files)} file(s).\n")

    for file in files:
        print(
            f"Name      : {file['name']}\n"
            f"Extension : {file['extension']}\n"
            f"Size      : {file['size']} bytes\n"
        )

    return files