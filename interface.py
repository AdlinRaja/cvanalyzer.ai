import streamlit as st 
from analysis import analyze_resume
st.title('CV Analyzer')

st.header('''This page helps you to compare your resume with the job description''')


st.sidebar.subheader('Drop your resume here')

pdf_doc=st.sidebar.file_uploader('Click here to Browse',type=['pdf'])

st.sidebar.markdown('Designed by Adlin Raja')
st.sidebar.markdown('https://www.linkedin.com/in/adlin-raja-d-272515226/')

job_des=st.text_area('Copy paste the Job description here',max_chars=10000)

submit=st.button('Generate ATS score')

if submit:
    with st.spinner('Getting results...'):
        analyze_resume(pdf_doc,job_des)