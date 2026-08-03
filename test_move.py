from tools.move_tool import MoveTool

tool = MoveTool()

result = tool.execute(
    "photo.jpg",
    "Images"
)

print("\nReturned Result\n")

print(result)