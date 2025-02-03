from pdfminer.high_level import extract_text
from config import configure

pdfs_directory = configure.temp_dir

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())


def load_pdf(file_path):
    text = extract_text(file_path)
    return text

