from src.memory import AgentMemory


memory = AgentMemory(
    "logs/test_memory.json"
)


# ==================================
# START CLEAN
# ==================================

memory.clear()


# ==================================
# TEST 1 — REMEMBER
# ==================================

entry = memory.remember(
    file_name="example.txt",
    action="move",
    status="verified",
    iteration=1,
    destination="Documents",
    message="File moved successfully."
)

print("\nTEST 1 — REMEMBER")

print(entry)


# ==================================
# TEST 2 — GET ALL
# ==================================

all_memory = memory.get_all()

print("\nTEST 2 — GET ALL")

print(all_memory)


# ==================================
# TEST 3 — FILE HISTORY
# ==================================

history = memory.get_file_history(
    "example.txt"
)

print("\nTEST 3 — FILE HISTORY")

print(history)