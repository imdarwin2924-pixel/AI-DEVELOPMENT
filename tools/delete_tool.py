from pathlib import Path


class DeleteTool:

    def execute(self, source_folder, file_name):

        file_path = Path(source_folder) / file_name

        if not file_path.exists():
            raise FileNotFoundError(f"{file_name} not found.")

        file_path.unlink()

        print(f"\n✔ Deleted {file_name}")

        return {
            "status": "success",
            "action": "delete",
            "file": file_name,
            "dry_run": False
        }