from src.agent import DirectoryCleanupAgent
from src.memory import AgentMemory


FOLDER = "data/memory_test_folder"
MEMORY_FILE = "logs/test_memory_agent.json"


print("\n" + "=" * 60)
print("DAY 11 — MEMORY-AWARE AGENT RUN 2")
print("=" * 60)


# ==================================
# LOAD EXISTING MEMORY
# ==================================

memory = AgentMemory(
    MEMORY_FILE
)


print("\nExisting Memory:")

for entry in memory.get_all():

    print(entry)


# ==================================
# CREATE AGENT
# ==================================

agent = DirectoryCleanupAgent(
    FOLDER
)


# Use the existing memory
agent.memory = memory
agent.planner.memory = memory
agent.observer.memory = memory


# ==================================
# RUN AGENT
# ==================================

print("\n" + "=" * 60)
print("RUNNING SECOND ITERATION")
print("=" * 60)

results = agent.run()


# ==================================
# DISPLAY RESULTS
# ==================================

print("\n" + "=" * 60)
print("RUN 2 RESULTS")
print("=" * 60)

for result in results:

    print(result)


# ==================================
# DISPLAY UPDATED MEMORY
# ==================================

print("\n" + "=" * 60)
print("UPDATED MEMORY")
print("=" * 60)

for entry in memory.get_all():

    print(entry)