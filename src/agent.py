from src.perceive import perceive
from src.planner import Planner
from src.executor import Executor
from src.logger import log_iteration
from src.observer import Observer
from src.loop_controller import LoopController
from src.plan_validator import PlanValidator
from src.memory import AgentMemory


class DirectoryCleanupAgent:

    def __init__(self, folder_path):

        self.folder_path = folder_path
        self.iteration = 0

        # ==================================
        # MEMORY
        # ==================================

        self.memory = AgentMemory(
            "logs/memory.json"
        )

        # ==================================
        # PLANNER
        # ==================================

        self.planner = Planner(
            memory=self.memory
        )

        # ==================================
        # EXECUTOR
        # ==================================

        self.executor = Executor()

        # ==================================
        # OBSERVER
        # ==================================

        self.observer = Observer(
            memory=self.memory
        )

        # ==================================
        # LOOP CONTROLLER
        # ==================================

        self.loop_controller = LoopController(
            max_iterations=5
        )

        # ==================================
        # PLAN VALIDATOR
        # ==================================

        self.validator = PlanValidator()

    def run(self):

        print("=" * 60)
        print("        DIRECTORY CLEAN-UP AGENT")
        print("=" * 60)

        # ==================================
        # AGENT LOOP
        # ==================================

        while self.loop_controller.can_continue():

            self.loop_controller.start_iteration()

            self.iteration = self.loop_controller.current_iteration

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
                # SUCCESS CONDITION - EMPTY FOLDER
                # ==================================

                if not files:

                    print("\n" + "=" * 50)
                    print("CLEANUP COMPLETED SUCCESSFULLY")
                    print("=" * 50)
                    print("No files remaining to process.")

                    log_iteration(
                        iteration=self.iteration,
                        stage="Agent Loop",
                        status="Completed",
                        details="No files remaining in the folder."
                    )

                    return []

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
                # VALIDATE PLAN
                # ==================================

                print("\n========== VALIDATION STAGE ==========\n")

                validation = self.validator.validate(
                    plan=plan,
                    source_folder=self.folder_path
                )

                if not validation["valid"]:

                    print("❌ Plan validation failed.")

                    for error in validation["errors"]:

                        print(f"   - {error}")

                    log_iteration(
                        iteration=self.iteration,
                        stage="Validate",
                        status="Failed",
                        details="; ".join(validation["errors"])
                    )

                    return []
                    
                print("✅ Plan validation passed.")

                log_iteration(
                    iteration=self.iteration,
                    stage="Validate",
                    status="Success",
                    details="Plan validation passed."
                )
                # ==================================
                # CONFIRMATION
                # ==================================

                print("\n" + "=" * 50)
                print("CONFIRMATION")
                print("=" * 50)

                choice = input(
                    "\nApply these changes? (yes/no): "
                ).strip().lower()

                if choice not in ("yes", "y"):

                    print("\nExecution cancelled by user.")

                    log_iteration(
                        iteration=self.iteration,
                        stage="Act",
                        status="Cancelled",
                        details="User cancelled execution."
                    )

                    return []

                # ==================================
                # ACT
                # ==================================

                print("\nExecuting cleanup...\n")

                results = self.executor.execute_plan(
                    plan=plan,
                    source_folder=self.folder_path,
                    dry_run=False
                )

                log_iteration(
                    iteration=self.iteration,
                    stage="Act",
                    status="Success",
                    details=f"Executed {len(results)} actions."
                )

                # ==================================
                # OBSERVE
                # ==================================

                observations = self.observer.observe(
                    source_folder=self.folder_path,
                    results=results,
                    iteration=self.iteration
                )
 
                self.observer.save_report(observations)

                log_iteration(
                    iteration=self.iteration,
                    stage="Observe",
                    status="Success",
                    details=f"Verified {len(observations)} actions."
                )

                # ==================================
                # EXECUTION SUMMARY
                # ==================================

                print("\n" + "=" * 50)
                print("EXECUTION SUMMARY")
                print("=" * 50)

                success = 0
                failed = 0
                ignored = 0

                for observation in observations:

                    if observation["status"] == "verified":

                        success += 1

                    elif observation["status"] == "ignored":

                        ignored += 1

                    else:

                        failed += 1

                    print(observation)

                print("\n" + "=" * 50)
                print("FINAL REPORT")
                print("=" * 50)

                print(f"Total Actions : {len(results)}")
                print(f"Successful    : {success}")
                print(f"Ignored       : {ignored}")
                print(f"Failed        : {failed}")

                # ==================================
                # LOOP DECISION
                # ==================================

                should_continue = (
                    self.loop_controller.should_continue(
                        observations
                    )
                )

                # ==================================
                # CLEANUP COMPLETED
                # ==================================

                if not should_continue:

                    if self.loop_controller.is_cleanup_complete(
                        observations
                    ):

                        print("\n" + "=" * 50)
                        print("CLEANUP COMPLETED SUCCESSFULLY")
                        print("=" * 50)

                        log_iteration(
                            iteration=self.iteration,
                            stage="Agent Loop",
                            status="Completed",
                            details="Cleanup success condition satisfied."
                        )

                        return observations

                    # ==================================
                    # MAXIMUM ITERATIONS REACHED
                    # ==================================

                    if self.loop_controller.is_max_iterations_reached():

                        print("\n" + "=" * 50)
                        print("MAXIMUM ITERATIONS REACHED")
                        print("=" * 50)

                        log_iteration(
                            iteration=self.iteration,
                            stage="Agent Loop",
                            status="Stopped",
                            details="Maximum iteration limit reached."
                        )

                        return observations

                # ==================================
                # CONTINUE TO NEXT ITERATION
                # ==================================

                print("\n" + "=" * 50)
                print("CLEANUP NOT COMPLETED")
                print("=" * 50)

                print("Failed actions detected.")

                if self.loop_controller.can_continue():

                    print("\nStarting next iteration...")

            except Exception as error:

                log_iteration(
                    iteration=self.iteration,
                    stage="Agent",
                    status="Failed",
                    details=str(error)
                )

                print(f"\nError : {error}")

                # ==================================
                # RETRY AFTER ERROR
                # ==================================

                if self.loop_controller.can_continue():

                    print("\nAttempting another iteration...")

                else:

                    print("\nMaximum iterations reached.")

        # ==================================
        # MAXIMUM ITERATIONS REACHED
        # ==================================

        print("\n" + "=" * 50)
        print("MAXIMUM ITERATIONS REACHED")
        print("=" * 50)

        log_iteration(
            iteration=self.iteration,
            stage="Agent Loop",
            status="Stopped",
            details="Maximum iteration limit reached."
        )

        return []