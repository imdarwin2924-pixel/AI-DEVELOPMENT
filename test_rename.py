from tools.rename_tool import RenameTool

tool = RenameTool()

result = tool.execute(
    "IMG001.jpg",
    "Vacation_2026.jpg"
)

print("\nReturned Result\n")

print(result)