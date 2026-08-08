import json
from pathlib import Path

from src.memory import AgentMemory


class Observer:

    def __init__(self, memory=None):

        self.memory = memory or AgentMemory()

    # ==================================
    # REMEMBER OBSERVATION
    # ==================================

    def remember_observation(
        self,
        observation,
        iteration
    ):

        self.memory.remember(

            file_name=observation.get("file"),

            action=observation.get("action"),

            status=observation.get("status"),

            iteration=iteration,

            destination=observation.get(
                "destination"
            ),

            message=observation.get(
                "message",
                ""
            )
        )

    # ==================================
    # OBSERVE
    # ==================================

    def observe(
        self,
        source_folder,
        results,
        iteration=1
    ):

        observations = []

        print("\n" + "=" * 50)
        print("OBSERVE STAGE")
        print("=" * 50)

        for result in results:

            action = result.get("action")
            status = result.get("status")

            # -------------------------
            # FAILED ACTIONS
            # -------------------------

            if status == "failed":

                message = result.get(
                    "error",
                    "Unknown error"
                )

                print(
                    f"✖ Failed: {result.get('file')}"
                )

                observations.append({
                    "file": result.get("file"),
                    "action": action,
                    "status": "failed",
                    "message": message
                })

                continue

            # -------------------------
            # IGNORED FILES
            # -------------------------

            if status == "ignored":

                message = (
                    f"ℹ Ignored: {result['file']}"
                )

                print(message)

                observations.append({
                    "file": result["file"],
                    "action": "ignore",
                    "status": "ignored",
                    "message": message
                })

                continue

            # -------------------------
            # MOVE
            # -------------------------

            if action == "move":

                destination = (
                    Path(source_folder)
                    / result["destination"]
                    / result["file"]
                )

                verified = destination.exists()

                message = (
                    f"✔ Verified: "
                    f"{result['file']} moved successfully."
                    if verified
                    else
                    f"✖ Verification failed: "
                    f"{result['file']} was not moved."
                )

                print(message)

                observations.append({
                    "file": result["file"],
                    "action": "move",
                    "status": (
                        "verified"
                        if verified
                        else "failed"
                    ),
                    "destination": result[
                        "destination"
                    ],
                    "message": message
                })

            # -------------------------
            # RENAME
            # -------------------------

            elif action == "rename":

                destination = (
                    Path(source_folder)
                    / result["new_name"]
                )

                verified = destination.exists()

                message = (
                    f"✔ Verified: "
                    f"{result['old_name']} renamed "
                    f"to {result['new_name']}."
                    if verified
                    else
                    f"✖ Verification failed: "
                    f"{result['old_name']} "
                    f"rename unsuccessful."
                )

                print(message)

                observations.append({
                    "file": result["new_name"],
                    "action": "rename",
                    "status": (
                        "verified"
                        if verified
                        else "failed"
                    ),
                    "destination": result[
                        "new_name"
                    ],
                    "message": message
                })

            # -------------------------
            # DELETE
            # -------------------------

            elif action == "delete":

                deleted = not (
                    Path(source_folder)
                    / result["file"]
                ).exists()

                message = (
                    f"✔ Verified: "
                    f"{result['file']} "
                    f"deleted successfully."
                    if deleted
                    else
                    f"✖ Verification failed: "
                    f"{result['file']} still exists."
                )

                print(message)

                observations.append({
                    "file": result["file"],
                    "action": "delete",
                    "status": (
                        "verified"
                        if deleted
                        else "failed"
                    ),
                    "message": message
                })

        # ==================================
        # SAVE TO MEMORY
        # ==================================

        for observation in observations:

            self.remember_observation(
                observation,
                iteration
            )

        return observations

    # ==================================
    # SAVE OBSERVATION REPORT
    # ==================================

    def save_report(self, observations):

        logs_folder = Path("logs")

        logs_folder.mkdir(
            exist_ok=True
        )

        report_path = (
            logs_folder
            / "observation_report.json"
        )

        with open(
            report_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                observations,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(
            "\n✅ Observation report saved:"
        )

        print(report_path)