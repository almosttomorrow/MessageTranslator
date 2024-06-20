import streamlit as st
from PyPDF2 import PdfReader
import openai
import zipfile
import io
import requests

openai.api_key = 'YOUR_OPENAI_API_KEY'

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def generate_mt564(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Please convert the following text into a Swift corporate action maessage (MT564 notification). Only include the MT564 message, nothing else in your answer. See PDF text:\n\n{text}"}
        ],
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_json = response.json()
    if 'choices' in response_json:
        return response_json['choices'][0]['message']['content'].strip()
    else:
        return "Error in response: " + str(response_json)

def main():
    st.title("Batch PDF to MT564 Translator")
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        st.success("Upload complete")
        if st.button("Create MT564"):
            mt564_messages = []
            for uploaded_file in uploaded_files:
                text = extract_text_from_pdf(uploaded_file)
                mt564_message = generate_mt564(text)
                mt564_messages.append((uploaded_file.name, mt564_message))
                st.write(f"MT564 Message for {uploaded_file.name}:")
                st.code(mt564_message)

            if st.button("Download All MT564 Messages"):
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as zf:
                    for file_name, mt564_message in mt564_messages:
                        zf.writestr(f"{file_name.replace('.pdf', '_MT564.txt')}", mt564_message)
                zip_buffer.seek(0)
                st.download_button(
                    label="Download ZIP",
                    data=zip_buffer,
                    file_name="mt564_messages.zip",
                    mime="application/zip"
                )

if __name__ == "__main__":
    main()
