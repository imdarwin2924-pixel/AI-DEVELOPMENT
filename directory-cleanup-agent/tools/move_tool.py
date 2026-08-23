import shutil
from pathlib import Path


class MoveTool:

    def execute(self, source_folder, file_name, destination):

        source = Path(source_folder) / file_name
        destination_folder = Path(source_folder) / destination

        destination_folder.mkdir(exist_ok=True)

        destination_file = destination_folder / file_name

        shutil.move(str(source), str(destination_file))

        print(f"\n✔ Moved {file_name} → {destination}")

        return {
            "status": "success",
            "action": "move",
            "file": file_name,
            "destination": destination,
            "dry_run": False
        }