"""
Move Tool

Currently runs in DRY RUN mode.
No files are actually moved.
"""


class MoveTool:

    def execute(self, file_name, destination):

        print("\n[DRY RUN]")
        print(f"Move File : {file_name}")
        print(f"Destination : {destination}")

        return {
            "status": "success",
            "action": "move",
            "file": file_name,
            "destination": destination,
            "dry_run": True
        }