"""
Delete Tool

Currently runs in DRY RUN mode.
No files are actually deleted.
"""


class DeleteTool:

    def execute(self, file_name):

        print("\n[DRY RUN]")
        print(f"Delete File : {file_name}")

        return {
            "status": "success",
            "action": "delete",
            "file": file_name,
            "dry_run": True
        }