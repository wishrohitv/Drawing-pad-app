# import datetime
#
# current_time = datetime.datetime.now().time()
# greeting = 'Good Morning..' if current_time.hour < 12 else 'Good Afternoon'
#
# print(greeting)
import os
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform

# from jnius import autoclass, cast


class PDFViewerApp(App):
    def open_pdf_external_viewer_android(self, pdf_file_path):
        if platform == 'android':
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')

            file_uri = Uri.parse(pdf_file_path)
            intent = Intent(Intent.ACTION_VIEW)
            intent.setDataAndType(file_uri, 'application/pdf')
            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK)

            current_activity = cast('android.app.Activity', PythonActivity.mActivity)
            current_activity.startActivity(intent)
        else:
            print("Opening PDF externally is only supported on Android.")

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Button to open the PDF using the default viewer
        open_button = Button(text="Open PDF")
        open_button.bind(on_press=self.open_pdf)
        layout.add_widget(open_button)

        return layout

    def open_pdf(self, instance):
        pdf_file_path = 'pd.pdf'  # Replace with the actual PDF file path

        if os.path.exists(pdf_file_path):
            if platform == 'android':
                # self.open_pdf_external_viewer_android(pdf_file_path)
                pass
            else:
                webbrowser.open(pdf_file_path)
        else:
            print("PDF file not found!")


if __name__ == '__main__':
    PDFViewerApp().run()
