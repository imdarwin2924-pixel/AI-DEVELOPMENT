from pathlib import Path


class PlanValidator:

    VALID_ACTIONS = {
        "move",
        "delete",
        "rename",
        "ignore"
    }
    def is_safe_destination(self, source_path, destination):

        if not destination:
            return False

        source_path = Path(source_path).resolve()

        destination_path = (
            source_path / destination
        ).resolve()

        try:

            destination_path.relative_to(source_path)

            return True

        except ValueError:

            return False

    def validate(self, plan, source_folder):

        errors = []

        source_path = Path(source_folder)

        # ----------------------------------
        # Check plan
        # ----------------------------------

        if not isinstance(plan, list):

            return {
                "valid": False,
                "errors": ["Plan must be a list."]
            }

        # ----------------------------------
        # Track files
        # ----------------------------------

        planned_files = set()

        # ----------------------------------
        # Validate each action
        # ----------------------------------

        for item in plan:

            file_name = item.get("file")
            action = item.get("action")

            # ----------------------------------
            # File name validation
            # ----------------------------------

            if not file_name:

                errors.append(
                    "Missing file name in plan item."
                )

                continue

            # ----------------------------------
            # Duplicate action detection
            # ----------------------------------

            if file_name in planned_files:

                errors.append(
                    f"Duplicate/conflicting action for '{file_name}'."
                )

            else:

                planned_files.add(file_name)

            # ----------------------------------
            # Action validation
            # ----------------------------------

            if action not in self.VALID_ACTIONS:

                errors.append(
                    f"Invalid action '{action}' for '{file_name}'."
                )

                continue

            # ----------------------------------
            # Source file validation
            # ----------------------------------

            file_path = source_path / file_name

            if not file_path.exists():

                errors.append(
                    f"File does not exist: {file_name}"
                )

                continue

            # ----------------------------------
            # MOVE validation
            # ----------------------------------

            if action == "move":

                destination = item.get("destination")

                if not destination:

                    errors.append(
                        f"Move destination missing for '{file_name}'."
                    )

                elif not self.is_safe_destination(
                    source_path,
                    destination
                ):

                    errors.append(
                        f"Unsafe destination for '{file_name}': "
                        f"{destination}"
                    )
            # ----------------------------------
            # RENAME validation
            # ----------------------------------

            elif action == "rename":

                new_name = item.get("new_name")

                if not new_name:

                    errors.append(
                        f"New name missing for '{file_name}'."
                    )

            # ----------------------------------
            # DELETE validation
            # ----------------------------------

            elif action == "delete":

                if not file_path.is_file():

                    errors.append(
                        f"Cannot delete non-file: {file_name}"
                    )

        # ----------------------------------
        # Final result
        # ----------------------------------

        if errors:

            return {
                "valid": False,
                "errors": errors
            }

        return {
            "valid": True,
            "errors": []
        }