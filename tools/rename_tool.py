from pathlib import Path


class RenameTool:

    def execute(self, source_folder, old_name, new_name):

        source = Path(source_folder) / old_name
        destination = Path(source_folder) / new_name

        source.rename(destination)

        print(f"\n✔ Renamed {old_name} → {new_name}")

        return {
            "status": "success",
            "action": "rename",
            "old_name": old_name,
            "new_name": new_name,
            "dry_run": False
        }