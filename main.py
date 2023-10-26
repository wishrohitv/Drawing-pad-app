import json
import os
import time
import kivy
import pdfplumber
import requests
import wikipedia
import plyer
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition
from kivy.core.window import Window
from kivy.core.text import LabelBase, Label
from kivy.clock import Clock
from database.database import get_chapter_database, download_pdf_file_to_local, create_an_new_account, get_user_data
from database.sign_in_user import sign_in_with_email_and_password

kivy.require('2.2.1')

LabelBase.register(name='Poppins',
                   fn_regular='Poppins-Regular.ttf',
                   fn_bold='Poppins-Bold.ttf',
                   fn_italic='Poppins-Italic.ttf',
                   fn_bolditalic='Poppins-BoldItalic.ttf')

Builder.load_file('components/widgets/nav_bar.kv')
Builder.load_file('components/widgets/rounded_button.kv')
# Builder.load_file('components/widgets/home_subjects.kv')
# Builder.load_file('components/widgets/chapter_list.kv')
Builder.load_file('components/widgets/classes_tabs.kv')
Builder.load_file('components/widgets/ninth_window_decorator.kv')
Builder.load_file('components/widgets/custom_text_input.kv')
Builder.load_file('components/widgets/admin_upload_panel.kv')

subject_name = []
image_link_id = []
class_name = []
chapter_name_pdf = []
global_user_id = []


class MainWindow(Screen):
    def on_pre_enter(self, *args):
        with open('user.json') as r:
            user_local_data = json.load(r)

        # Clock.schedule_once(self.change_screen, .00000001)
        # self.manager.current = "Main"

    def change_screen(self, *args):
        self.manager.current = "Second"

    def login(self, email, passw):
        try:
            token = sign_in_with_email_and_password(email, passw)
            print(token)
            uid = token.get("localId")
            get_user_data(uid)

            # uid saving
            if uid is not None:
                with open('user_id.txt', 'w') as save_id:
                    save_id.write(uid)

            with open('user_id.txt') as re:
                t = re.read()
            global global_user_id
            global_user_id.append(t)

            self.manager.current = 'Second'

        except Exception as error:
            print(error)
            self.ids.notice_banner.text = "No Internet!"
            self.ids.notice_banner.opacity = 100
            plyer.notification.notify(
                title="No Internet!",
                message="please connect to internet!"
                # app_icon=r"
            )


class SecondWindow(Screen):
    greeting = StringProperty()

    def on_pre_enter(self):

        self.greeting_time()
        Clock.schedule_once(self.greeting_message, 4)
        Clock.schedule_once(self.upload_r, 0.00001)

    def upload_r(self, *args):
        global global_user_id
        with open('user.json') as se:
            seco = json.load(se)
            print(type(seco.get(global_user_id[-1])["post_right"]))
        if global_user_id[-1]:
            self.ids.upload_right.disabled = False
            self.ids.upload_right.opacity = 100

    def greeting_time(self):
        current_time = time.localtime().tm_hour
        if current_time < 12:
            self.greeting = 'Good Morning'
        elif 12 <= current_time < 18:
            self.greeting = 'Good Afternoon'
        elif 18 <= current_time <= 20:
            self.greeting = 'Good Evening '
        elif 20 < current_time <= 24:
            self.greeting = 'Good Night   '

    def greeting_message(self, *args):
        self.greeting = 'by Rahul sir!   '

    def forthWB(self):
        sm = App.get_running_app().root.ids.sm
        sm.current = "Forth"

    def thirdWB(self, subject):
        global subject_name
        subject_name.append(subject)
        sm = App.get_running_app().root.ids.sm
        sm.get_screen('Third').ids.nav_name.text = f"{subject}         "
        sm.current = "Third"


# second windows widget
class HomeSubjects(GridLayout):
    pass


class ThirdWindow(Screen):
    subject_details = ListProperty([])

    def on_enter(self, *args):
        # with open('demo/demo.json') as f:
        #     data = json.load(f)
        #     self.subject_details = [
        #             {'text': str(x), 'chapter_name': data[x]['name'], 'upload_date': data[x]["upload_date"],
        #              'link': data[x]['link']} for x in data]
        # classmate-classes

        data = get_chapter_database(subject_name[-1])

        try:
            self.subject_details = [
                {'text': f"{data[x]['chapter_name']} {data[x]['class']}", "class_": data[x]['class'],
                 'chapter_name': data[x]['chapter_name'],
                 'upload_date': data[x]["upload_date"],
                 'pdf_cloud_dir': data[x]['data_path_dir']} for x in data.keys()]
        except Exception as f:
            print(f, "me")
            self.notice_me()

    def notice_me(self):
        self.manager.transition = NoTransition()
        self.manager.current = "Eight"


class EachChapterButton(Button):
    def on_release(self):
        sm = App.get_running_app().root.ids.sm
        sm.get_screen('Ninth').ids.chapter_index.text = self.text
        sm.get_screen('Ninth').ids.chapter_name.text = self.chapter_name
        sm.get_screen('Ninth').ids.class_.text = self.class_
        sm.get_screen('Ninth').ids.upload_date.text = f"{self.upload_date}\non uploaded"
        sm.get_screen('Ninth').ids.pdf_cloud_dir.text = self.pdf_cloud_dir
        sm.current = 'Ninth'


class ForthWindow(Screen):
    pass


class FifthWindow(Screen):
    def on_pre_enter(self):
        with open("LicenceCopy.txt", 'r') as f:
            licence_copy = f.read()
            self.ids.java.text = str(licence_copy)


class SixthWindow(Screen):

    def save_user_data(self, new_name, new_class, new_email, new_passw, new_passw2):

        if new_passw == new_passw2:
            create_an_new_account(new_name, new_class, new_email, new_passw)
            self.manager.current = "Main"

        else:
            self.ids.create_pass.text = "password are not same!"


class SeventhWindow(Screen):
    profile = StringProperty()

    def on_pre_enter(self, *args):
        with open('user.json') as v:
            name = json.load(v)
        self.profile = "assets/images/default_avatar.jpg"
        self.ids.user_name.text = str(name.get(global_user_id[-1])["name"])
        self.ids.user_name.color = "blue"


class EighthWindow(Screen):

    def on_pre_enter(self, *args):
        self.ids.notice_sub.text = f"{subject_name[-1]}         "


class NinthWindow(Screen):
    def view_pdf_image(self, link, class_, chapter_name):
        global image_link_id, class_name, chapter_name_pdf
        image_link_id.append(link)
        class_name.append(class_)
        chapter_name_pdf.append(chapter_name)
        sm = App.get_running_app().root.ids.sm
        # sm.get_screen('Tenth').ids.image = link
        sm.current = 'Tenth'


class PdfImage(BoxLayout):
    image_source = StringProperty()


class TenthWindow(Screen):
    image_source = StringProperty()
    pdf_image_list = ListProperty([])

    def on_pre_enter(self):
        global image_link_id
        download_pdf_file_to_local(image_link_id[-1], class_name[-1])

        # pdf file to image operation

        path1 = f"pdf_image_view/{image_link_id[-1]}_1.png"
        images = os.path.isfile(path1)
        if not images:

            pdf_file_path = f"chapter_visual_data/{image_link_id[-1]}.pdf"
            # Open the PDF file with pdfplumber
            with pdfplumber.open(pdf_file_path) as pdf:
                # Iterate through each page and convert it to an image
                for page_num in range(len(pdf.pages)):
                    page = pdf.pages[page_num]
                    image_data = page.to_image()

                    # Save the image as a file (you can customize the filename)
                    image_filename = f"{image_link_id[-1]}_{page_num + 1}.png"
                    image_data.save(f"pdf_image_view/{image_filename}", format="PNG")

        # iteration pdf as image

        l = pdfplumber.open(f"chapter_visual_data/{image_link_id[-1]}.pdf")
        m = len(l.pages)

        self.ids.pdf_screen.text = f"{chapter_name_pdf[-1]}   {class_name[-1]}"
        self.pdf_image_list = [{"image_source": f"pdf_image_view/{image_link_id[-1]}_{i}.png"} for i in range(1, m + 1)]


class SearchWindow(Screen):
    def wiki(self, quarry):
        try:
            check = requests.get("http://www.google.com")
            if check.status_code == 200:
                if quarry != "":
                    self.ids.search_button.background_color = .5, .2, .3, 1
                    try:
                        results = wikipedia.summary(quarry, auto_suggest=False)

                    except wikipedia.WikipediaException as e:
                        self.ids.result.text = str(f'Ask me like this!\n{e}')

                    else:
                        self.ids.result.text = str(results)
                        self.ids.search_button.background_color = 130 / 255, 70 / 255, 0, 1

            else:
                self.ids.result.text = "no internet\ncheck your internet connectivity"

        except:
            self.ids.result.text = "no internet\ncheck your internet connectivity"


class AdminPanel(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# Navigation Buttons
class ReturnHomeButton(Button):
    def on_release(self):
        sm = App.get_running_app().root.ids.sm
        sm.current = "Second"


kv = Builder.load_file("muwtru.kv")


class MiniApp(App):
    def build(self):
        Window.clearcolor = [0 / 255, 128 / 255, 128 / 255, 1]
        Window.size = [300, 620]
        self.title = 'Classmate classes'
        return kv

    # def on_start(self):
    #     self.root.dispatch('on_enter')


subhi = MiniApp()
subhi.run()
