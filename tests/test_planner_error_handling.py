from src.planner import Planner


# ==========================================
# MOCK RESPONSE
# ==========================================

class MockResponse:

    def __init__(self, text):
        self.text = text


# ==========================================
# MOCK CLIENT
# ==========================================

class MockModels:

    def __init__(self, response=None, error=None):
        self.response = response
        self.error = error

    def generate_content(self, model, contents):

        if self.error:
            raise self.error

        return MockResponse(self.response)


class MockClient:

    def __init__(self, response=None, error=None):

        self.models = MockModels(
            response=response,
            error=error
        )


# ==========================================
# TEST FILES
# ==========================================

files = [
    {
        "name": "test.jpg",
        "extension": ".jpg",
        "size": 0
    }
]


# ==========================================
# TEST 1 — API FAILURE
# ==========================================

print("\nTEST 1 — GEMINI API FAILURE")

planner = Planner()
planner.client = MockClient(
    error=Exception("Simulated API failure")
)

try:

    planner.generate_plan(files)

    print("❌ TEST FAILED — Error was not raised")

except RuntimeError as error:

    print(f"✅ TEST PASSED — {error}")


# ==========================================
# TEST 2 — EMPTY RESPONSE
# ==========================================

print("\nTEST 2 — EMPTY RESPONSE")

planner = Planner()
planner.client = MockClient(
    response=""
)

try:

    planner.generate_plan(files)

    print("❌ TEST FAILED — Empty response accepted")

except ValueError as error:

    print(f"✅ TEST PASSED — {error}")


# ==========================================
# TEST 3 — INVALID JSON
# ==========================================

print("\nTEST 3 — INVALID JSON")

planner = Planner()
planner.client = MockClient(
    response="This is not JSON"
)

try:

    planner.generate_plan(files)

    print("❌ TEST FAILED — Invalid JSON accepted")

except ValueError as error:

    print(f"✅ TEST PASSED — {error}")


# ==========================================
# TEST 4 — MISSING FILE
# ==========================================

print("\nTEST 4 — MISSING FILE")

planner = Planner()

planner.client = MockClient(
    response='''[
        {
            "file": "another.jpg",
            "action": "move",
            "destination": "Images",
            "reason": "Image file"
        }
    ]'''
)

try:

    planner.generate_plan(files)

    print("❌ TEST FAILED — Missing file accepted")

except ValueError as error:

    print(f"✅ TEST PASSED — {error}")


# ==========================================
# TEST 5 — VALID RESPONSE
# ==========================================

print("\nTEST 5 — VALID RESPONSE")

planner = Planner()

planner.client = MockClient(
    response='''[
        {
            "file": "test.jpg",
            "action": "move",
            "destination": "Images",
            "reason": "Image file"
        }
    ]'''
)

try:

    plan = planner.generate_plan(files)

    print("GENERATED PLAN:")
    print(plan)

    print("✅ TEST PASSED")

except Exception as error:

    print(f"❌ TEST FAILED — {error}")


print("\n" + "=" * 50)
print("PLANNER ERROR HANDLING TEST COMPLETED")
print("=" * 50)