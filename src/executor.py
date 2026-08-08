from tools.move_tool import MoveTool
from tools.rename_tool import RenameTool
from tools.delete_tool import DeleteTool


class Executor:

    def __init__(self):

        self.move_tool = MoveTool()
        self.rename_tool = RenameTool()
        self.delete_tool = DeleteTool()

    def execute_plan(self, plan, source_folder, dry_run=True):

        results = []

        print("\n========== ACT STAGE ==========\n")

        for action in plan:

            action_type = action.get("action", "").lower()

            try:

                # --------------------------
                # MOVE
                # --------------------------

                if action_type == "move":

                    if dry_run:

                        print(f"[DRY RUN] Move {action['file']} -> {action['destination']}")

                        result = {
                            "status": "success",
                            "action": "move",
                            "file": action["file"],
                            "destination": action["destination"],
                            "dry_run": True
                        }

                    else:

                        result = self.move_tool.execute(
                            source_folder,
                            action["file"],
                            action["destination"]
                        )

                # --------------------------
                # RENAME
                # --------------------------

                elif action_type == "rename":

                    if dry_run:

                        print(f"[DRY RUN] Rename {action['file']} -> {action['destination']}")

                        result = {
                            "status": "success",
                            "action": "rename",
                            "file": action["file"],
                            "destination": action["destination"],
                            "dry_run": True
                        }

                    else:

                        result = self.rename_tool.execute(
                            source_folder,
                            action["file"],
                            action["destination"]
                        )

                # --------------------------
                # DELETE
                # --------------------------

                elif action_type == "delete":

                    if dry_run:

                        print(f"[DRY RUN] Delete {action['file']}")

                        result = {
                            "status": "success",
                            "action": "delete",
                            "file": action["file"],
                            "dry_run": True
                        }

                    else:

                        result = self.delete_tool.execute(
                            source_folder,
                            action["file"]
                        )

                # --------------------------
                # IGNORE
                # --------------------------

                elif action_type == "ignore":

                    print(f"[IGNORE] {action['file']}")

                    result = {
                        "status": "ignored",
                        "action": "ignore",
                        "file": action["file"]
                    }

                else:

                    result = {
                        "status": "failed",
                        "action": action_type,
                        "file": action.get("file")
                    }

            except Exception as error:

                result = {
                    "status": "failed",
                    "action": action_type,
                    "file": action.get("file"),
                    "error": str(error)
                }

            results.append(result)

        return results