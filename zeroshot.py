import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file.")
client = genai.Client(api_key=api_key)
feedback="the product is excellent ,and delivery was very fast"
prompt=f""" 
classify customer feedback positive negtive, or netural or give one reason
{feedback}
"""
response=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)
print("\nGemini Response:\n")
print(response.text)