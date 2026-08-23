from src.agent import DirectoryCleanupAgent


print("\n" + "=" * 50)
print("AGENT ERROR HANDLING TEST")
print("=" * 50)


class FailingPlanner:

    def generate_plan(self, files):

        raise RuntimeError(
            "Simulated Planner failure"
        )


agent = DirectoryCleanupAgent(
    "data/sample_folder"
)

# Replace the real planner with a failing planner
agent.planner = FailingPlanner()


print("\nTEST — PLANNER FAILURE")

try:

    result = agent.run()

    print("\nRESULT:")
    print(result)

    print(
        "\n✅ TEST PASSED — "
        "Agent handled Planner failure."
    )

except Exception as error:

    print(
        "\n❌ TEST FAILED — "
        f"Unhandled exception: {error}"
    )


print("\n" + "=" * 50)
print("AGENT ERROR HANDLING TEST COMPLETED")
print("=" * 50)