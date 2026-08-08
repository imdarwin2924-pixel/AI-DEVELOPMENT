from src.memory import AgentMemory


MEMORY_FILE = "logs/test_persistence.json"


# ==================================
# FIRST RUN
# ==================================

memory = AgentMemory(MEMORY_FILE)

memory.clear()

memory.remember(
    file_name="first_test.txt",
    action="delete",
    status="verified",
    iteration=1,
    message="Deleted successfully."
)

print("\nFIRST RUN")
print(memory.get_all())


# ==================================
# SIMULATE PROGRAM RESTART
# ==================================

del memory


# ==================================
# SECOND RUN
# ==================================

memory = AgentMemory(MEMORY_FILE)

print("\nSECOND RUN")
print(memory.get_all())


# ==================================
# VERIFY PERSISTENCE
# ==================================

history = memory.get_file_history(
    "first_test.txt"
)

print("\nFILE HISTORY")
print(history)


if len(history) == 1:

    print("\n✅ MEMORY PERSISTENCE TEST PASSED")

else:

    print("\n❌ MEMORY PERSISTENCE TEST FAILED")