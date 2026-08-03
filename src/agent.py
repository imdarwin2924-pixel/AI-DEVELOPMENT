from src.perceive import perceive
from src.planner import Planner
from src.executor import Executor
from src.logger import log_iteration


class DirectoryCleanupAgent:

    def __init__(self, folder_path):

        self.folder_path = folder_path
        self.iteration = 1

        self.planner = Planner()
        self.executor = Executor()

    def run(self):

        print("=" * 60)
        print("        DIRECTORY CLEAN-UP AGENT")
        print("=" * 60)

        try:

            # ==================================
            # PERCEIVE
            # ==================================

            files = perceive(self.folder_path)

            log_iteration(
                iteration=self.iteration,
                stage="Perceive",
                status="Success",
                details=f"Found {len(files)} files."
            )

            # ==================================
            # PLAN
            # ==================================

            print("\n========== PLAN STAGE ==========\n")

            plan = self.planner.generate_plan(files)

            print("Cleanup Plan\n")

            for item in plan:

                print("-----------------------------------")
                print(f"File        : {item['file']}")
                print(f"Action      : {item['action']}")
                print(f"Destination : {item.get('destination', '')}")
                print(f"Reason      : {item['reason']}")

            log_iteration(
                iteration=self.iteration,
                stage="Plan",
                status="Success",
                details=f"Generated {len(plan)} actions."
            )

            # ==================================
            # ACT
            # ==================================

            results = self.executor.execute_plan(plan)

            log_iteration(
                iteration=self.iteration,
                stage="Act",
                status="Success",
                details=f"Executed {len(results)} dry-run actions."
            )

            # ==================================
            # SUMMARY
            # ==================================

            print("\n========== SUMMARY ==========\n")

            for result in results:

                print(result)

            return results

        except Exception as error:

            log_iteration(
                iteration=self.iteration,
                stage="Agent",
                status="Failed",
                details=str(error)
            )

            print(f"\nError : {error}")

            return []