# Batch PDF to MT564 Translator

This application allows users to upload multiple PDF files containing corporate action announcements and translates them into MT564 message format using OpenAI's GPT-4 model.

## Features

- Batch upload PDF files
- Generate MT564 messages for each PDF
- Download all generated MT564 messages as a ZIP file

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/batch-pdf-to-mt564.git
   cd batch-pdf-to-mt564
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the provided URL in your browser, upload PDF files, and generate MT564 messages.

## Requirements

- Python 3.10+
- PyPDF2
- Streamlit
- OpenAI
- Requests

## License

This project is licensed under the MIT License.
.