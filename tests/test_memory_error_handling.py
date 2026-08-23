import json
from pathlib import Path

from src.memory import AgentMemory


TEST_MEMORY_FILE = Path(
    "logs/test_memory_error.json"
)


def cleanup():

    if TEST_MEMORY_FILE.exists():
        TEST_MEMORY_FILE.unlink()


# ==========================================
# TEST 1 — MISSING FILE
# ==========================================

print("\nTEST 1 — MISSING MEMORY FILE")

cleanup()

memory = AgentMemory(
    str(TEST_MEMORY_FILE)
)

print("Memory:", memory.get_all())

if memory.get_all() == []:

    print("✅ TEST PASSED")

else:

    print("❌ TEST FAILED")


# ==========================================
# TEST 2 — VALID MEMORY
# ==========================================

print("\nTEST 2 — VALID MEMORY")

with open(
    TEST_MEMORY_FILE,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        [
            {
                "file": "example.txt",
                "action": "delete",
                "status": "verified",
                "iteration": 1
            }
        ],
        file,
        indent=4
    )


memory = AgentMemory(
    str(TEST_MEMORY_FILE)
)

print("Memory:", memory.get_all())

if len(memory.get_all()) == 1:

    print("✅ TEST PASSED")

else:

    print("❌ TEST FAILED")


# ==========================================
# TEST 3 — CORRUPTED JSON
# ==========================================

print("\nTEST 3 — CORRUPTED JSON")

with open(
    TEST_MEMORY_FILE,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        '{"invalid": "json"'
    )


memory = AgentMemory(
    str(TEST_MEMORY_FILE)
)

print("Recovered memory:")
print(memory.get_all())

if memory.get_all() == []:

    print(
        "✅ TEST PASSED — "
        "Corrupted memory safely reset."
    )

else:

    print("❌ TEST FAILED")


# ==========================================
# TEST 4 — WRONG DATA TYPE
# ==========================================

print("\nTEST 4 — WRONG MEMORY FORMAT")

with open(
    TEST_MEMORY_FILE,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        {
            "file": "example.txt",
            "action": "delete"
        },
        file,
        indent=4
    )


memory = AgentMemory(
    str(TEST_MEMORY_FILE)
)

print("Recovered memory:")
print(memory.get_all())

if memory.get_all() == []:

    print(
        "✅ TEST PASSED — "
        "Invalid memory structure handled."
    )

else:

    print("❌ TEST FAILED")


# ==========================================
# TEST 5 — MEMORY CAN RECOVER AFTER RESET
# ==========================================

print("\nTEST 5 — MEMORY RECOVERY")

memory.remember(
    file_name="recovered.txt",
    action="move",
    status="verified",
    iteration=1,
    destination="Documents",
    message="Recovered successfully."
)

history = memory.get_latest_file_history(
    "recovered.txt"
)

print("Recovered history:")
print(history)

if history is not None:

    print(
        "✅ TEST PASSED — "
        "Memory can be written after recovery."
    )

else:

    print("❌ TEST FAILED")


# ==========================================
# CLEANUP
# ==========================================

cleanup()

print("\n" + "=" * 50)
print("MEMORY ERROR HANDLING TEST COMPLETED")
print("=" * 50)