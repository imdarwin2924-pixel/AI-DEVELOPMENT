from tools.rename_tool import RenameTool

tool = RenameTool()

tool.execute(
    source_folder="data/sample_folder",
    old_name="report.docx",
    new_name="project_report.docx"
)