import os


def scan_directory(folder_path):
    """
    Scan the given directory and collect file information.
    """

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    files = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isfile(full_path):
            file_info = {
                "name": item,
                "extension": os.path.splitext(item)[1],
                "size": os.path.getsize(full_path),
                "path": full_path
            }

            files.append(file_info)

    return files