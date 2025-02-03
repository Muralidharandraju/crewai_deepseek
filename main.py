from crew import TopicIdentifier
import streamlit as st
from utils.preprocess import load_pdf,upload_pdf
import agentops
from config import configure
pdfs_directory = configure.temp_dir

## streamlit app
st.title("Smart ATS")
st.text("Identify topics in given pdf")
uploaded_file=st.file_uploader("Upload pdf ",type="pdf",help="Please uplaod the pdf")
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        upload_pdf(uploaded_file)
        text = load_pdf(pdfs_directory + uploaded_file.name)
        inputs = {input : text}
        st.subheader(inputs)

        # agentops.init()
        # TopicIdentifier().crew().kickoff(inputs=text)