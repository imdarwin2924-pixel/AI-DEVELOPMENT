from src.executor import Executor

plan = [

    {
        "file": "IMG001.jpg",
        "action": "move",
        "destination": "Images"
    },

    {
        "file": "old_file.tmp",
        "action": "delete"
    }
]

executor = Executor()

results = executor.execute_plan(
    plan=plan,
    source_folder="data/sample_folder",
    dry_run=False
)

print("\nResults\n")

for item in results:

    print(item)