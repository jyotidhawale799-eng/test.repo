import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file.")
client = genai.Client(api_key=api_key)
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    course: str
    sentiment: Literal["Positive", "Negative", "Neutral"]
    rating: int = Field(ge=1, le=5)

feedback_text="""
The python course is excellent
I rate it 4 out of 5
"""

prompt=f""""
   Analyze this student feedback.

   Extract:
   -course
   -sentiment
   -rating

   Feedback:
   {feedback_text}
"""

response=client.models.generate_content(
    model="gemini-3.6-flash",
    #contents=prompt,
    #config={"response_mime_type": "application/json",
        "response_schema": Feedback}
)
   

print(response.text)