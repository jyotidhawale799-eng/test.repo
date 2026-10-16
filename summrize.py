import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file.")
client = genai.Client(api_key=api_key)
article="""The Iran–Iraq War, also called the First Imposed War,[57][58][59] Eight-Year War,[60][61] or Sacred Defense[62] by Iran, began with the Iraqi invasion of Iran in September 1980. After eight years of conflict, both countries accepted a ceasefire deal brokered by the United Nations, which became effective in August 1988. The war caused around 500,000 deaths (excluding numbers from the related Anfal campaign), making it the deadliest conventional war ever fought between regular armies of developing countries.In starting the war, the Iraqi government—led by President Saddam Hussein—primarily wanted to prevent Ruhollah Khomeini, Iran's leader following the 1979 Iranian Revolution, from exporting Iran's new state ideology to Iraq. Iraq also feared that Iran, being a theocratic state mostly composed of Shia Muslims, would rally Iraq's Shia majority against the Sunni Muslim-controlled Baʽathist government. Iraq also wished to replace Iran as the main national power in the Persian Gulf. The war followed a long-running history of border disputes between the two states, as a result of which Iraq planned to retake the eastern bank of the Shatt al-Arab river that it had ceded to Iran in the 1975 Algiers Agreement.

"""
prompt=f"""summrize the above article in 50 words
{article}"""
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)
print("\nGemini Response:\n")
print(response.text)