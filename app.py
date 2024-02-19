import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  # Load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey! Act like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science,
data analysis, and big data engineering. Your task is to evaluate the resume based 
on the given job description. Consider the job market is very competitive,
and you should provide the best assistance for improving the resumes.
Assign the percentage match based on JD and
the missing keywords with high accuracy.
resume: {text}
description: {jd}

I want the response in one single string having the structure
{{"JD Match": "%", "Missing Keywords": [], "Profile Summary": ""}}
"""

# Streamlit App
st.title("Smart ATS 📄💼")
st.text("Improve Your Resume with Smart ATS")

jd = st.text_area("Paste the Job Description ✍️")
uploaded_file = st.file_uploader("Upload Your Resume (PDF) 📤", type="pdf", help="Please upload the PDF")

submit = st.button("Submit 🚀")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))
        st.subheader("The Response is:")
        st.json(json.loads(response))
