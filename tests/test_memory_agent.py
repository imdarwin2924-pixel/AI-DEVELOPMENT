from src.agent import DirectoryCleanupAgent
from src.memory import AgentMemory


FOLDER = "data/memory_test_folder"
MEMORY_FILE = "logs/test_memory_agent.json"


# ==================================
# CREATE CLEAN TEST MEMORY
# ==================================

memory = AgentMemory(
    MEMORY_FILE
)

memory.clear()


# ==================================
# CREATE AGENT
# ==================================

agent = DirectoryCleanupAgent(
    FOLDER
)

# Use isolated test memory
agent.memory = memory
agent.planner.memory = memory
agent.observer.memory = memory


# ==================================
# DISPLAY INITIAL STATE
# ==================================

print("\n" + "=" * 60)
print("DAY 11 — MEMORY-AWARE AGENT TEST")
print("=" * 60)

print("\nInitial files:")

for item in memory.get_all():
    print(item)


# ==================================
# RUN AGENT
# ==================================

print("\n" + "=" * 60)
print("RUNNING AGENT")
print("=" * 60)

results = agent.run()


# ==================================
# DISPLAY RESULTS
# ==================================

print("\n" + "=" * 60)
print("AGENT RESULTS")
print("=" * 60)

for result in results:
    print(result)


# ==================================
# DISPLAY MEMORY
# ==================================

print("\n" + "=" * 60)
print("AGENT MEMORY")
print("=" * 60)

for entry in memory.get_all():
    print(entry)


# ==================================
# MEMORY COUNT
# ==================================

print("\nTotal memory entries:")
print(len(memory.get_all()))