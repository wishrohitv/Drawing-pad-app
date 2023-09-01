from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from pdf2image import convert_from_path
import PyPDF2

class PDFViewerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        pdf_widget = PDFWidget()
        layout.add_widget(pdf_widget)
        pdf_widget.load_pdf('pd.pdf')  # Replace with the actual PDF file path
        return layout

class PDFWidget(Image):
    def load_pdf(self, pdf_path):
        pdf_images = convert_from_path(pdf_path)
        if pdf_images:
            # Assuming you want to display only the first page of the PDF
            self.texture = pdf_images[0].texture
            self.reload()

if __name__ == '__main__':
    PDFViewerApp().run()
