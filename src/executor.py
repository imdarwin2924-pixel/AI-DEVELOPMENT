from tools.move_tool import MoveTool
from tools.rename_tool import RenameTool
from tools.delete_tool import DeleteTool


class Executor:

    def __init__(self):

        self.move_tool = MoveTool()
        self.rename_tool = RenameTool()
        self.delete_tool = DeleteTool()

    def execute_plan(self, plan):

        results = []

        print("\n========== ACT STAGE (DRY RUN) ==========\n")

        for action in plan:

            action_type = action.get("action", "").lower()

            if action_type == "move":

                result = self.move_tool.execute(
                    action["file"],
                    action["destination"]
                )

            elif action_type == "rename":

                result = self.rename_tool.execute(
                    action["file"],
                    action["destination"]
                )

            elif action_type == "delete":

                result = self.delete_tool.execute(
                    action["file"]
                )

            elif action_type == "ignore":

                print(f"\n[IGNORE] {action['file']}")

                result = {
                    "status": "ignored",
                    "action": "ignore",
                    "file": action["file"],
                    "dry_run": True
                }

            else:

                print(f"\nUnknown action : {action_type}")

                result = {
                    "status": "failed",
                    "action": action_type,
                    "file": action.get("file"),
                    "dry_run": True
                }

            results.append(result)

        return results