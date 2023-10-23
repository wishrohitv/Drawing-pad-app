from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class ImageLoaderApp(App):
    def build(self):
        # Create a BoxLayout as the root widget
        self.root = BoxLayout(orientation='vertical')

        url = "https://storage.googleapis.com/classmate-classes.appspot.com/image.jpg"

        def on_success(req, result):
            # Create an AsyncImage with the loaded URL
            image = AsyncImage(source=url)  # Use the URL directly as the source
            self.root.add_widget(image)

        def on_error(req, error):
            print("Error loading image:", error)

        req = UrlRequest(url, on_success=on_success, on_error=on_error)
        return self.root


if __name__ == '__main__':
    app = ImageLoaderApp()
    app.run()
