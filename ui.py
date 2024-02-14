import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_handler import convert_pdf_to_docx
from docx_handler import convert_docx_to_pdf

class ConverterGUI:
    def __init__(self, root):
        self.root = root
        root.title('File Converter')

        # Tamaño de la ventana
        root.geometry('400x200')

        # Fondo de la ventana
        root.config(bg = '#1A936F')

        # Botón para convertir de PDF a DOCX
        self.btn_convert_pdf = tk.Button(root, text='Convert PDF to DOCX', command=self.convert_to_docx, style="BW.TButton")
        self.btn_convert_pdf.pack(pady=20)

        #Botón para convertir de DOCX a PDF
        self.btn_convert_docx = tk.Button(root, text='Convert DOCX to PDF', command=self.convert_to_pdf, style="BW.TButton")
        self.btn_convert_docx.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        return file_path

    def convert_to_docx(self):
        pdf_file = self.select_file()
        if pdf_file:
            try:
                result = convert_pdf_to_docx(pdf_file)
                messagebox.showinfo('Conversion completed', f'The DOCX file has been created in {result}')
            except Exception as e:
                messagebox.showerror('Error', f'The conversion has failed: {e}')

    def convert_to_pdf(self):
        docx_file = self.select_file()
        if docx_file:
            try:
                result = convert_docx_to_pdf(docx_file)
                messagebox.showinfo('Conversion completed', f'The PDF file has been created in {result}')
            except Exception as e:
                messagebox.showerror('Error', f'The conversion has failed: {e}')

def main():
    root = tk.Tk()
    app = ConverterGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()