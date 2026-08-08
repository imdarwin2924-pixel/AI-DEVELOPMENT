from src.memory import AgentMemory


MEMORY_FILE = "logs/test_latest_memory.json"


memory = AgentMemory(
    MEMORY_FILE
)

memory.clear()


# ==================================
# ADD HISTORY
# ==================================

memory.remember(
    file_name="report.pdf",
    action="move",
    status="verified",
    iteration=1,
    destination="Documents",
    message="Moved successfully."
)

memory.remember(
    file_name="report.pdf",
    action="move",
    status="verified",
    iteration=2,
    destination="Documents",
    message="Already processed."
)

memory.remember(
    file_name="report.pdf",
    action="rename",
    status="verified",
    iteration=3,
    destination="final_report.pdf",
    message="Renamed successfully."
)


# ==================================
# GET FULL HISTORY
# ==================================

print("\nFULL HISTORY")

history = memory.get_file_history(
    "report.pdf"
)

for item in history:

    print(item)


# ==================================
# GET LATEST
# ==================================

print("\nLATEST HISTORY")

latest = memory.get_latest_file_history(
    "report.pdf"
)

print(latest)


# ==================================
# VERIFY
# ==================================

if latest["iteration"] == 3:

    print(
        "\n✅ LATEST MEMORY TEST PASSED"
    )

else:

    print(
        "\n❌ LATEST MEMORY TEST FAILED"
    )