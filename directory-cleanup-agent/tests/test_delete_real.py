from tools.delete_tool import DeleteTool

tool = DeleteTool()

tool.execute(
    source_folder="data/sample_folder",
    file_name="old_file.tmp"
)