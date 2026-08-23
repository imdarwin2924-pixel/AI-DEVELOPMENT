from src.agent import DirectoryCleanupAgent


def main():
    """
    Entry point of the Directory Cleanup Agent.
    """

    folder_path = "data/sample_folder"

    agent = DirectoryCleanupAgent(folder_path)
    agent.run()


if __name__ == "__main__":
    main()