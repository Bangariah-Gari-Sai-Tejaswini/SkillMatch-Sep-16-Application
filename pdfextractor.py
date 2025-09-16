from pypdf import PdfReader

def text_extractor(file):
    pdf_file = PdfReader(file)   # pass UploadedFile directly
    pdf_text = ""
    for page in pdf_file.pages:
        pdf_text += page.extract_text() or ""
    return pdf_text
