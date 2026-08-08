from src.memory import AgentMemory
from src.planner import Planner


MEMORY_FILE = "logs/test_memory_aware_planner.json"


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
# CURRENT FILES
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
    },

    {
        "name": "temporary.tmp",
        "extension": ".tmp",
        "size": 0
    }
]


# ==================================
# GENERATE PLAN
# ==================================

print("\n" + "=" * 50)
print("MEMORY-AWARE GEMINI PLANNER TEST")
print("=" * 50)

plan = planner.generate_plan(files)


# ==================================
# DISPLAY PLAN
# ==================================

print("\nGENERATED PLAN")

for item in plan:

    print("-----------------------------------")
    print(f"File        : {item.get('file')}")
    print(f"Action      : {item.get('action')}")
    print(f"Destination : {item.get('destination', '')}")
    print(f"Reason      : {item.get('reason', '')}")


# ==================================
# VALIDATE PLAN TYPE
# ==================================

if not isinstance(plan, list):

    print("\n❌ TEST FAILED")
    raise SystemExit(1)


# ==================================
# REQUIRED FILES
# ==================================

required_files = {
    "report.pdf",
    "new_image.jpg",
    "temporary.tmp"
}


planned_files = {
    item.get("file")
    for item in plan
}
# ==================================
# CHECK MEMORY-BASED DECISION
# ==================================

report_plan = None
image_plan = None
temp_plan = None

for item in plan:

    if item.get("file") == "report.pdf":
        report_plan = item

    elif item.get("file") == "new_image.jpg":
        image_plan = item

    elif item.get("file") == "temporary.tmp":
        temp_plan = item


print("\nMEMORY-BASED DECISIONS")

print("\nreport.pdf:")
print(report_plan)

print("\nnew_image.jpg:")
print(image_plan)

print("\ntemporary.tmp:")
print(temp_plan)


# ==================================
# VERIFY REPORT.PDF
# ==================================

if report_plan is None:

    print(
        "\n❌ report.pdf missing from plan"
    )

    raise SystemExit(1)


if report_plan.get("action") != "ignore":

    print(
        "\n❌ MEMORY TEST FAILED"
    )

    print(
        "report.pdf was previously processed "
        "successfully but planner did not ignore it."
    )

    raise SystemExit(1)


# ==================================
# VERIFY IMAGE
# ==================================

if image_plan is None:

    print(
        "\n❌ new_image.jpg missing from plan"
    )

    raise SystemExit(1)


if image_plan.get("action") != "move":

    print(
        "\n❌ IMAGE TEST FAILED"
    )

    print(
        "new_image.jpg should be moved."
    )

    raise SystemExit(1)


if image_plan.get("destination") != "Images":

    print(
        "\n❌ IMAGE DESTINATION TEST FAILED"
    )

    raise SystemExit(1)


# ==================================
# VERIFY TEMP FILE
# ==================================

if temp_plan is None:

    print(
        "\n❌ temporary.tmp missing from plan"
    )

    raise SystemExit(1)


if temp_plan.get("action") != "delete":

    print(
        "\n❌ TEMP FILE TEST FAILED"
    )

    raise SystemExit(1)


print(
    "\n✅ MEMORY DECISION TEST PASSED"
)


print("\nINPUT FILES:")
print(required_files)

print("\nPLANNED FILES:")
print(planned_files)


# ==================================
# CHECK MISSING FILES
# ==================================

missing_files = (
    required_files - planned_files
)


if missing_files:

    print(
        "\n❌ TEST FAILED"
    )

    print(
        f"Missing files: {missing_files}"
    )

    raise SystemExit(1)


# ==================================
# CHECK EXTRA FILES
# ==================================

extra_files = (
    planned_files - required_files
)


if extra_files:

    print(
        "\n❌ TEST FAILED"
    )

    print(
        f"Unexpected files: {extra_files}"
    )

    raise SystemExit(1)


# ==================================
# SUCCESS
# ==================================

print(
    "\n✅ MEMORY-AWARE PLANNER TEST PASSED"
)