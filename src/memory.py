import json
from pathlib import Path
from datetime import datetime


class AgentMemory:

    def __init__(self, memory_file="logs/memory.json"):

        self.memory_file = Path(memory_file)

        self.memory_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.memory = self._load_memory()

    # ==================================
    # LOAD MEMORY
    # ==================================

    def _load_memory(self):

        if not self.memory_file.exists():

            return []

        try:

            with open(
                self.memory_file,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                if isinstance(data, list):
                    return data

                print(
                    "⚠ Memory file does not contain a list."
                )

                return []

        except json.JSONDecodeError:

            print(
                "⚠ Memory file contains invalid JSON. "
                "Starting with empty memory."
            )

            return []

        except OSError as error:

            print(
                f"⚠ Could not read memory file: {error}"
            )

            return []

    # ==================================
    # SAVE MEMORY
    # ==================================

    def _save_memory(self):

        try:

            with open(
                self.memory_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.memory,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except OSError as error:

            print(
                f"⚠ Could not save memory: {error}"
            )

            return False

    # ==================================
    # REMEMBER
    # ==================================

    def remember(
        self,
        file_name,
        action,
        status,
        iteration,
        destination=None,
        message=""
    ):

        entry = {

            "timestamp": datetime.now().isoformat(),

            "iteration": iteration,

            "file": file_name,

            "action": action,

            "status": status,

            "destination": destination,

            "message": message
        }

        self.memory.append(entry)

        saved = self._save_memory()

        if not saved:

            print(
                f"⚠ Memory entry could not be persisted "
                f"for: {file_name}"
            )

        return entry

    # ==================================
    # GET ALL MEMORY
    # ==================================

    def get_all(self):

        return self.memory

    # ==================================
    # FIND FILE HISTORY
    # ==================================

    def get_file_history(self, file_name):

        return [
            entry
            for entry in self.memory
            if entry.get("file") == file_name
        ]

    # ==================================
    # GET LATEST FILE HISTORY
    # ==================================

    def get_latest_file_history(self, file_name):

        history = self.get_file_history(
            file_name
        )

        if not history:

            return None

        return history[-1]

    # ==================================
    # CLEAR MEMORY
    # ==================================

    def clear(self):

        self.memory = []

        self._save_memory()