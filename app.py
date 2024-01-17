import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
from dotenv import load_dotenv
from streamlit_lottie import st_lottie 
import json
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

st.title("----- 💡 Welcome to TalentED 😎 ------")
st.text("👉🏻                  Personal ATS for Job-Seekers & Recruiters                   👈")
with open('animation.json') as anim_source:
    animation = json.load(anim_source)
st_lottie(animation, 1, True, True, "high", 350, -200)
st.text_input("Job Role")
desc = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Pls Upload PDF file Only")
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number] 
            text += str(page.extract_text())

        input_prompt = f'''
        You're a skilled ATS (Applicant Tracking System) Scanner with a deep understanding of tech roles, software development, 
        tech consulting, and understand the ATS role in-depth. Your task is to evaluate the resume against the given description. 
        You must consider that the job market is crowded with applications and you should only pick the best talent. 
        Thus, assign the percentage & MissingKeywords with honesty & accuracy
        resume: {text}
        description: {desc}
        I want a output in one single string having the structure: {{"PercentageMatch": "%", "MissingKeywordsintheResume": [], "ProfileSummary": ""}}.
        '''

        with st.spinner("Evaluating Profile..."):
            response = model.generate_content(input_prompt)
        response_data = json.loads(response.text)
        # st.write(response.text)

        st.subheader("ATS Scanner Dashboard")
        st.subheader("Candidate Evaluation Results")
        st.text(f"Percentage Match: {response_data['PercentageMatch']}")
        st.subheader("Missing Keywords in the Resume")
        for keyword in response_data['MissingKeywordsintheResume']:
            st.text(keyword)
        st.subheader("Profile Summary")
        st.markdown(response_data['ProfileSummary'])

