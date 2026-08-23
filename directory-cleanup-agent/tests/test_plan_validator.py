from src.plan_validator import PlanValidator


validator = PlanValidator()


# ==================================
# TEST 1 — VALID PLAN
# ==================================

plan = [
    {
        "file": "test_image.jpg",
        "action": "move",
        "destination": "Images"
    },

    {
        "file": "test_temp.tmp",
        "action": "delete"
    },

    {
        "file": "random.zip",
        "action": "ignore"
    }
]


result = validator.validate(
    plan,
    "data/sample_folder"
)

print("\nTEST 1 — VALID PLAN")
print(result)


# ==================================
# TEST 2 — INVALID ACTION
# ==================================

plan = [
    {
        "file": "IMG001.jpg",
        "action": "compress"
    }
]


result = validator.validate(
    plan,
    "data/sample_folder"
)

print("\nTEST 2 — INVALID ACTION")
print(result)


# ==================================
# TEST 3 — MISSING DESTINATION
# ==================================

plan = [
    {
        "file": "test_image.jpg",
        "action": "move"
    }
]


result = validator.validate(
    plan,
    "data/sample_folder"
)

print("\nTEST 3 — MISSING DESTINATION")
print(result)
# ==================================
# TEST 4 — DUPLICATE ACTION
# ==================================

plan = [
    {
        "file": "test_image.jpg",
        "action": "move",
        "destination": "Images"
    },

    {
        "file": "test_image.jpg",
        "action": "delete"
    }
]


result = validator.validate(
    plan,
    "data/sample_folder"
)

print("\nTEST 4 — DUPLICATE ACTION")
print(result)
# ==================================
# TEST 5 — UNSAFE DESTINATION
# ==================================

plan = [
    {
        "file": "test_image.jpg",
        "action": "move",
        "destination": "../outside_folder"
    }
]


result = validator.validate(
    plan,
    "data/sample_folder"
)

print("\nTEST 5 — UNSAFE DESTINATION")
print(result)   