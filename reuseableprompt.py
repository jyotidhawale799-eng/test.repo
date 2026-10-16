import os
import time
import csv
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Add GEMINI_API_KEY to your .env file.")
client = genai.Client(api_key=api_key)
def create_prompt(topic, audience, output_format):
    return f"""
    Act as an experienced technical educator.

    Topic: {topic}
    Target audience: {audience}
    Output format: {output_format}

    Instructions:
    1. Explain the concept accurately.
    2. Include one practical example.
    3. Use language appropriate for the audience.
    4. End with one practice question.
    """

def generate_lesson(topic, audience, output_format):
    prompt = create_prompt(topic, audience, output_format)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    print("\nGENERATED LESSON\n")
    print(response.text)


if __name__ == "__main__":
    generate_lesson(
        topic="Python exception handling",
        audience="First-year engineering students",
        output_format="Headings and bullet points"
    )