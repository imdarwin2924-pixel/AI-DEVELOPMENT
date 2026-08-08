from src.executor import Executor

plan = [

    {
        "file": "photo.jpg",
        "action": "move",
        "destination": "Images"
    },

    {
        "file": "movie.mp4",
        "action": "move",
        "destination": "Videos"
    },

    {
        "file": "temp.tmp",
        "action": "delete",
        "destination": ""
    },

    {
        "file": "notes.pdf",
        "action": "ignore",
        "destination": ""
    }
]

executor = Executor()

results = executor.execute_plan(plan)

print("\nExecution Results\n")

for result in results:

    print(result)