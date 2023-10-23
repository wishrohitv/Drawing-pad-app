import os
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.utils import platform
from jnius import autoclass, cast

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE,
    Permission.READ_EXTERNAL_STORAGE])


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
        file = FileChooserListView()
        # file.bind(on_selection=self.selected)
        button = Button(text="Open PDF", size_hint=(1, .3))
        button.bind(on_press=lambda x: self.open_file(file.selection))
        layout.add_widget(file)
        layout.add_widget(button)

        return layout

    def open_file(self, selection):
        print(selection)

    # def open_pdf(self, instance):
    #     pdf_file_path = 'pd.pdf'  # Replace with the actual PDF file path

        if os.path.exists(selection[-1]):
            if platform == 'android':
                self.open_pdf_external_viewer_android(selection[-1])
            else:
                webbrowser.open(selection[-1])
        else:
            print("PDF file not found!")

    def on_start(self, **kwargs):

        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])


if __name__ == '__main__':
    PDFViewerApp().run()
