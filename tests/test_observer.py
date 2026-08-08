from src.observer import Observer

results = [

    {
        "status": "success",
        "action": "move",
        "file": "IMG001.jpg",
        "destination": "Images"
    },

    {
        "status": "success",
        "action": "delete",
        "file": "old_file.tmp"
    }
]

observer = Observer()

observations = observer.observe(
    source_folder="data/sample_folder",
    results=results
)

print("\nObservation Report\n")

for item in observations:

    print(item)