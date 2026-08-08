import json

from google import genai

from src.config import GEMINI_API_KEY


class Planner:

    def __init__(self, memory=None):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.memory = memory

    # ==================================
    # MEMORY CONTEXT
    # ==================================

    def build_memory_context(self, files):

        if self.memory is None:

            return "No previous cleanup history available."

        memory_context = []

        for file in files:

            file_name = file.get("name")

            if not file_name:
                continue

            history = self.memory.get_latest_file_history(
                file_name
            )

            if history:

                memory_context.append({
                    "file": file_name,
                    "previous_action": history.get(
                        "action"
                    ),
                    "previous_status": history.get(
                        "status"
                    ),
                    "previous_destination": history.get(
                        "destination"
                    ),
                    "previous_iteration": history.get(
                        "iteration"
                    )
                })

        if not memory_context:

            return "No previous cleanup history available."

        return json.dumps(
            memory_context,
            indent=4
        )

    # ==================================
    # GENERATE PLAN
    # ==================================

    def generate_plan(self, files):

        memory_context = self.build_memory_context(
            files
        )

        prompt = f"""
You are an intelligent Directory Cleanup Agent.

Analyze EVERY file in the Current files list.

IMPORTANT OUTPUT RULES:

1. You MUST return exactly ONE plan item for EVERY input file.
2. Never omit a file.
3. The value of "file" MUST exactly match the input file name.
4. Return ONLY a valid JSON array.
5. Do not include Markdown or explanations outside the JSON array.
6. Even if a file was processed previously, it MUST still appear in the plan.
7. If a file was previously processed successfully, choose "ignore"
   instead of repeating the same action unnecessarily.
8. If previous processing failed, evaluate the file again.

Cleanup rules:

1. Images → move to Images
2. Videos → move to Videos
3. PDFs and DOCX → move to Documents
4. Temporary files (.tmp) → delete
5. Unknown files → ignore

Memory rules:

1. Review the previous cleanup history.
2. Use previous successful actions to avoid unnecessary repetition.
3. A previously successful file should normally be marked "ignore"
   if the previous action already completed the required cleanup.
4. Do not create conflicting actions for the same file.
5. Never use destinations outside the source folder.

For ignored files use:

{{
    "file": "example.xyz",
    "action": "ignore",
    "reason": "Already processed successfully"
}}

For files requiring cleanup use:

{{
    "file": "photo.jpg",
    "action": "move",
    "destination": "Images",
    "reason": "Image file"
}}

Previous cleanup history:

{memory_context}

Current files:

{json.dumps(files, indent=4)}
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):

            text = text.replace(
                "```json",
                ""
            )

            text = text.replace(
                "```",
                ""
            )

        elif text.startswith("```"):

            text = text.replace(
                "```",
                ""
            )

        text = text.strip()

        return json.loads(text)