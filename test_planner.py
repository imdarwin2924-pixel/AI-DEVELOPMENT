from src.perceive import perceive
from src.planner import Planner

folder = "data/sample_folder"

files = perceive(folder)

planner = Planner()

plan = planner.generate_plan(files)

print("\nCleanup Plan\n")

for item in plan:

    print(item)