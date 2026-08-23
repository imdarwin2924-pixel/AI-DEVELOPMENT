from src.agent import DirectoryCleanupAgent
from src.memory import AgentMemory


FOLDER = "data/sample_folder"


# ==================================
# CREATE MEMORY
# ==================================

memory = AgentMemory(
    "logs/test_real_memory.json"
)

memory.clear()


# ==================================
# CREATE AGENT
# ==================================

agent = DirectoryCleanupAgent(FOLDER)

# Replace the agent's memory with our test memory
agent.memory = memory
agent.observer.memory = memory


print("\n" + "=" * 50)
print("REAL AGENT MEMORY TEST")
print("=" * 50)


# ==================================
# RUN AGENT
# ==================================

results = agent.run()


# ==================================
# DISPLAY RESULTS
# ==================================

print("\n" + "=" * 50)
print("AGENT RESULTS")
print("=" * 50)

for result in results:
    print(result)


# ==================================
# DISPLAY MEMORY
# ==================================

print("\n" + "=" * 50)
print("MEMORY")
print("=" * 50)

for entry in memory.get_all():
    print(entry)