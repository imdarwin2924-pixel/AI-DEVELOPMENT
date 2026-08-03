import json
from google import genai

from src.config import GEMINI_API_KEY


class Planner:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_plan(self, files):

        prompt = f"""
You are an intelligent Directory Cleanup Agent.

Analyze every file.

Return ONLY JSON.

Rules:

1. Images → move to Images
2. Videos → move to Videos
3. PDFs and DOCX → move to Documents
4. Temporary files (.tmp) → delete
5. Unknown files → ignore

Return this format:

[
  {{
      "file":"photo.jpg",
      "action":"move",
      "destination":"Images",
      "reason":"Image file"
  }}
]

Files:

{json.dumps(files, indent=4)}
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "")

        elif text.startswith("```"):
            text = text.replace("```", "")

        text = text.strip()

        return json.loads(text)