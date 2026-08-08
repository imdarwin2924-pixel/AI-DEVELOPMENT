from src.observer import Observer
from src.memory import AgentMemory


memory = AgentMemory(
    "logs/test_observer_memory.json"
)

memory.clear()

observer = Observer(
    memory=memory
)


results = [

    {
        "status": "ignored",
        "action": "ignore",
        "file": "unknown.xyz",
        "dry_run": False
    }
]


# ==================================
# OBSERVE
# ==================================

observations = observer.observe(
    source_folder="data/sample_folder",
    results=results,
    iteration=1
)


print("\nOBSERVATIONS")
print(observations)


# ==================================
# MEMORY
# ==================================

print("\nMEMORY")
print(memory.get_all())