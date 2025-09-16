from pdfextractor import text_extractor
import streamlit as st
import google.generativeai as genai
import os

# Configure the model
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Upload resume
st.sidebar.title(':blue[Upload your resume(pdf only)]')
file = st.sidebar.file_uploader('Resume', type=['pdf'])

resume_text = ""  # Initialize to avoid NameError

if file:
    resume_text = text_extractor(file)
    st.write(resume_text)

# Main page
st.title(':orange[SKILLMATCH] : :blue[AI Assisted Skill Matching Tool]')
st.markdown('##### This application will match your resume and the job description.' \
            'It will create a detailed report on the match')

tips = '''
Follow these steps to proceed:
* Upload your resume in sidebar - PDF Only
* Copy and paste the job description for which you are applying
* Click the button and see the magic.
'''
st.write(tips)

job_desc = st.text_area('Copy and Paste Job Description here', max_chars=10000)

button = st.button("Click")

if button:
    if resume_text and job_desc:
        prompt = f'''
Assume you are a SkillMatch Expert and creating ATS Friendly profiles
Match the following resume with the job description
provided by the user's resume = {resume_text} and job description is 
{job_desc} 

* Give a brief description of about 3 to 5 lines of the applicant
* Give a range of expected ATS Score along with matching and non-matching keywords
* Give the chances of getting shortlisted for this position in percentage.
* Perform SWOT Analysis and discuss each and everything in bullet points
* Suggest what all improvements can be made in resume in order to get better ATS and increase 
selection percentage of short-listing
* Prepare a one page resume in such a format that can be copied and pasted in word and
converted to PDF 
* Also create two customised resumes as per the job description provided
* Use bullet points and tables where ever required.
'''
        response = model.generate_content(prompt)
        st.write(response.text)
    else:
        st.write("Please provide job description and upload resume")
