from src.loop_controller import LoopController


controller = LoopController(max_iterations=3)


# ----------------------------------
# TEST 1: SUCCESS
# ----------------------------------

successful_observations = [
    {
        "file": "IMG001.jpg",
        "action": "move",
        "status": "verified"
    },
    {
        "file": "temp.txt",
        "action": "ignore",
        "status": "ignored"
    }
]

print("\nTEST 1: SUCCESS")

print(
    "Should continue:",
    controller.should_continue(successful_observations)
)


# ----------------------------------
# TEST 2: FAILURE
# ----------------------------------

failed_observations = [
    {
        "file": "IMG001.jpg",
        "action": "move",
        "status": "failed"
    }
]

print("\nTEST 2: FAILURE")

controller.current_iteration = 1

print(
    "Should continue:",
    controller.should_continue(failed_observations)
)


# ----------------------------------
# TEST 3: MAX ITERATIONS
# ----------------------------------

print("\nTEST 3: MAXIMUM ITERATIONS")

controller.current_iteration = 3

print(
    "Should continue:",
    controller.should_continue(failed_observations)
)