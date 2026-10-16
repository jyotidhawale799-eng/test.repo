import os
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )


client = genai.Client(api_key=api_key)


pdf_file = "Jyoti_Sanjay_Dhawale_Resume.pdf"

if not os.path.exists(pdf_file):
    raise FileNotFoundError(
        "resume.pdf not found. Place your resume in this folder."
    )

reader = PdfReader(pdf_file)

resume_text = ""

for page in reader.pages:
    extracted_text = page.extract_text()
    if extracted_text:
        resume_text += extracted_text + "\n"

if not resume_text.strip():
    raise ValueError(
        "No readable text found in the PDF. "
        "Try using a text-based resume PDF."
    )

print("\n===== RESUME EXTRACTED SUCCESSFULLY =====")
print(resume_text)


prompt = f"""
You are an expert AI career advisor and technical recruiter.

Analyze the following resume and recommend suitable jobs
based on the candidate's actual qualifications.

RESUME:
{resume_text}

Perform these tasks:

1. Identify the candidate's educational qualifications.
2. Identify technical skills, programming languages,
   tools, certifications, and projects.
3. Identify relevant soft skills and experience.
4. Recommend the TOP 5 most suitable job roles.
5. For each job role, explain:
   - Job title
   - Why this job suits the candidate
   - Relevant skills already present in the resume
   - Missing skills the candidate should learn
   - Whether the job is suitable for a fresher
   - Entry-level responsibilities
   - A practical project to improve employability
6. Give a suitability score out of 100 for each role.
   Explain that these scores are estimates, not guarantees.
7. Suggest the best job role to target first.
8. Create a personalized 3-month learning roadmap.
9. Suggest suitable internships and entry-level positions.
10. Do not invent qualifications, certifications, projects,
    or work experience that are not in the resume.
11. If information is missing, clearly state what is unknown.
12. Distinguish between jobs the candidate can apply for now
    and jobs that require additional preparation.

Present the response with clear headings and bullet points.
Use simple English and practical advice.
"""


print("\n===== ANALYZING YOUR RESUME WITH GEMINI AI =====\n")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)


print("===== YOUR PERSONALIZED JOB RECOMMENDATIONS =====\n")
print(response.text)
print("\nRecommendations saved to job_recommendations.txt")