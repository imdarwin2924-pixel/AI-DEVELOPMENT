import json
import os


LOG_FILE = "logs/iterations.json"


def log_iteration(iteration, stage, status, details):
    """
    Save an iteration log to logs/iterations.json
    """

    os.makedirs("logs", exist_ok=True)

    log_entry = {
        "iteration": iteration,
        "stage": stage,
        "status": status,
        "details": details
    }

    logs = []

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            try:
                logs = json.load(file)
            except json.JSONDecodeError:
                logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

    print("\n✅ Log saved successfully.")