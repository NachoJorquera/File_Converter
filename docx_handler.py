from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def convert_docx_to_pdf(docx_path):
     # Carga el DOCX
    doc = Document(docx_path)
    # Crea un objeto canvas de ReportLab para el archivo PDF
    output_path = docx_path.replace('.docx', '_converted.pdf')
    c = canvas.Canvas(output_path, pagesize=letter)

    # Para simplificar se agregar todo el texto en una posición fija
    text_obj = c.beginText(40,750) # Posición inicial en la esquina superior izquierda.
    for paragraph in doc.paragraphs:
        text_obj.textLine(paragraph.text)

        c.drawText(text_obj)
        c.save()

        return output_path