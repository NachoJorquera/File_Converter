from PyPDF2 import PdfReader
from docx import Document

def convert_pdf_to_docx(pdf_path):
    # Crea un DOCX en blanco.
    doc = Document()
    # Abre el archivo PDF.
    reader = PdfReader(pdf_path)
    # Lee cada página del PDF.
    for page in reader.pages:
        # Extrae el texto de la página.
        text = page.extract_text()
        # Añade el texto a un parrafo en el DOCX.
        doc.add_paragraph(text)
    # Guarda el DOCX
        output_path = pdf_path.replace('.pdf', '_converted.docx')
        doc.save(output_path)
        return output_path