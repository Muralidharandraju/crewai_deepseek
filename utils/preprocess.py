from pdfminer.high_level import extract_text
from config import configure
import os

pdfs_directory = configure.temp_dir

#house keeping functions
def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())


def load_pdf(file_path):
    text = extract_text(file_path)
    return text

def create_folder_if_not_exists(folder_path):
    """
    Creates a folder if it does not exist.

    Args:
        folder_path: The path to the folder to create.
    """
    os.makedirs(folder_path, exist_ok=True)