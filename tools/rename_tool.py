"""
Rename Tool

Currently runs in DRY RUN mode.
No files are actually renamed.
"""


class RenameTool:

    def execute(self, old_name, new_name):

        print("\n[DRY RUN]")
        print(f"Rename File : {old_name}")
        print(f"New Name    : {new_name}")

        return {
            "status": "success",
            "action": "rename",
            "old_name": old_name,
            "new_name": new_name,
            "dry_run": True
        }