import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_resume(resume_text, user_goal):

    prompt = f"""
You are a senior software engineer and hiring manager.

Evaluate the following resume according to the user's career goal.

User Goal:
{user_goal}

Rules:
- Extract only relevant skills.
- Ignore unrelated technologies.
- Find missing skills.
- Generate a learning roadmap.
- Generate interview questions.

Return ONLY valid JSON in this format:

{{
    "skills": [],
    "missing_skills": [],
    "roadmap": [],
    "interview_questions": []
}}

Resume:

{resume_text}
"""

    try:

        response = model.generate_content(prompt)

        content = response.text.strip()

        start = content.find("{")
        end = content.rfind("}") + 1

        return json.loads(content[start:end])

    except Exception as e:

        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }