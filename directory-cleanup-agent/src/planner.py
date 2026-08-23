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

            try:

                history = self.memory.get_latest_file_history(
                    file_name
                )

            except Exception as error:

                print(
                    f"⚠ Memory lookup failed for "
                    f"{file_name}: {error}"
                )

                continue

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
    # CLEAN AI RESPONSE
    # ==================================

    def _clean_response(self, text):

        if not text:

            raise ValueError(
                "Gemini returned an empty response."
            )

        text = text.strip()

        # Remove Markdown code fences
        if text.startswith("```json"):

            text = text[len("```json"):]

            if text.endswith("```"):
                text = text[:-3]

        elif text.startswith("```"):

            text = text[3:]

            if text.endswith("```"):
                text = text[:-3]

        return text.strip()

    # ==================================
    # VALIDATE GENERATED PLAN
    # ==================================

    def _validate_plan(self, plan, files):

        if not isinstance(plan, list):

            raise ValueError(
                "Planner response must be a JSON array."
            )

        expected_files = {
            file.get("name")
            for file in files
            if file.get("name")
        }

        planned_files = {
            item.get("file")
            for item in plan
            if isinstance(item, dict)
        }

        missing_files = expected_files - planned_files

        if missing_files:

            raise ValueError(
                f"Planner omitted files: "
                f"{sorted(missing_files)}"
            )

        for item in plan:

            if not isinstance(item, dict):

                raise ValueError(
                    "Every plan item must be a JSON object."
                )

            if not item.get("file"):

                raise ValueError(
                    "Plan item is missing 'file'."
                )

            if not item.get("action"):

                raise ValueError(
                    f"Missing action for "
                    f"'{item.get('file')}'."
                )

        return plan

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
7. If a file was processed successfully, choose "ignore"
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

        # ==================================
        # GEMINI API CALL
        # ==================================

        try:

            response = self.client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        except Exception as error:

            raise RuntimeError(
                f"Gemini API request failed: {error}"
            ) from error

        # ==================================
        # RESPONSE EXTRACTION
        # ==================================

        try:

            text = response.text

        except Exception as error:

            raise ValueError(
                f"Unable to read Gemini response: {error}"
            ) from error

        # ==================================
        # CLEAN RESPONSE
        # ==================================

        try:

            text = self._clean_response(text)

        except Exception as error:

            raise ValueError(
                f"Invalid Gemini response: {error}"
            ) from error

        # ==================================
        # JSON PARSING
        # ==================================

        try:

            plan = json.loads(text)

        except json.JSONDecodeError as error:

            raise ValueError(
                f"Gemini returned invalid JSON: {error}"
            ) from error

        # ==================================
        # PLAN VALIDATION
        # ==================================

        return self._validate_plan(
            plan,
            files
        )