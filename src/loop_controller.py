class LoopController:

    def __init__(self, max_iterations=5):

        self.max_iterations = max_iterations
        self.current_iteration = 0

    def start_iteration(self):

        self.current_iteration += 1

        message = (
            "\n"
            + "=" * 50
            + "\n"
            + "ITERATION "
            + str(self.current_iteration)
            + "\n"
            + "=" * 50
        )

        print(message, flush=True)

    def can_continue(self):

        return self.current_iteration < self.max_iterations

    def is_max_iterations_reached(self):

        return self.current_iteration >= self.max_iterations

    def is_cleanup_complete(self, observations):

        if not observations:
            return True

        for observation in observations:

            if observation.get("status") == "failed":
                return False

        return True

    def should_continue(self, observations):

        # Cleanup is already complete
        if self.is_cleanup_complete(observations):
            return False

        # Maximum iterations reached
        if self.is_max_iterations_reached():
            return False

        # Cleanup is not complete and
        # another iteration is available
        return True