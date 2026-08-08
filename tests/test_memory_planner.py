from src.memory import AgentMemory
from src.planner import Planner


MEMORY_FILE = "logs/test_planner_memory.json"


# ==================================
# CREATE MEMORY
# ==================================

memory = AgentMemory(
    MEMORY_FILE
)

memory.clear()


# ==================================
# ADD PREVIOUS HISTORY
# ==================================

memory.remember(
    file_name="report.pdf",
    action="move",
    status="verified",
    iteration=1,
    destination="Documents",
    message="Moved successfully."
)


# ==================================
# CREATE PLANNER
# ==================================

planner = Planner(
    memory=memory
)


# ==================================
# TEST FILES
# ==================================

files = [

    {
        "name": "report.pdf",
        "extension": ".pdf",
        "size": 0
    },

    {
        "name": "new_image.jpg",
        "extension": ".jpg",
        "size": 0
    }
]


# ==================================
# BUILD MEMORY CONTEXT
# ==================================

context = planner.build_memory_context(
    files
)


print("\nMEMORY CONTEXT")
print(context)


# ==================================
# VERIFY
# ==================================

if "report.pdf" in context:

    print(
        "\n✅ MEMORY PLANNER TEST PASSED"
    )

else:

    print(
        "\n❌ MEMORY PLANNER TEST FAILED"
    )