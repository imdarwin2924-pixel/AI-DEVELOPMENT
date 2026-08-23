from src.plan_validator import PlanValidator


validator = PlanValidator()

print("\n" + "=" * 50)
print("AGENT VALIDATION TEST")
print("=" * 50)


# ==================================
# TEST 1 — VALID PLAN
# ==================================

valid_plan = [
    {
        "file": "validator_test.txt",
        "action": "move",
        "destination": "Images"
    }
]

result = validator.validate(
    valid_plan,
    "data/sample_folder"
)

print("\nTEST 1 — VALID PLAN")
print(result)


# ==================================
# TEST 2 — UNSAFE PLAN
# ==================================

unsafe_plan = [
    {
        "file": "validator_test.txt",
        "action": "move",
        "destination": "../outside_folder"
    }
]

result = validator.validate(
    unsafe_plan,
    "data/sample_folder"
)

print("\nTEST 2 — UNSAFE PLAN")
print(result)


# ==================================
# TEST 3 — CONFLICTING PLAN
# ==================================

conflicting_plan = [
    {
        "file": "validator_test.txt",
        "action": "move",
        "destination": "Images"
    },
    {
        "file": "validator_test.txt",
        "action": "delete"
    }
]

result = validator.validate(
    conflicting_plan,
    "data/sample_folder"
)

print("\nTEST 3 — CONFLICTING PLAN")
print(result)