import json
import time
import kivy
import wikipedia
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.core.image import ImageLoader

kivy.require('2.1.0')

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
image_link = []


class MainWindow(Screen):

    def login(self, name, passw):
        self.manager.current = 'Second'
        # from firebase import firebase
        # firebase = firebase.FirebaseApplication('https://classmate-classes-default-rtdb.firebaseio.com/', None)
        #
        # result = firebase.get('classmate-classes-default-rtdb/User', '')
        # for i in result.keys():
        #     if result[i]['Email'] == name.text:
        #         if result[i]['Password'] == passw.text:
        #
        #             print(result[i]['Email'], 'logged!')

        # else:
        #     pop = Popup(title='Invalid Form',
        #                 content=Label(text='data did\'nt match!.'),
        #                 size_hint=(None, None), size=(400, 200))
        #
        #     pop.open()


class SecondWindow(Screen):
    greeting = StringProperty()

    def on_pre_enter(self):
        self.greeting_time()
        Clock.schedule_once(self.greeting_message, 4)

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

    def on_pre_enter(self, *args):
        # print(subject_name[-1])
        # with open('demo/demo.json') as f:
        #     data = json.load(f)
        #     self.subject_details = [
        #         {'text': str(x), 'chapter_name': data[x]['name'], 'chapter_upload_date': data[x]["upload_date"],
        #          'link': data[x]['link']} for x in data]
        from firebase import firebase
        # classmate-classes
        firebase = firebase.FirebaseApplication('https://classmate-classes-f9057-default-rtdb.firebaseio.com/', None)
        data = firebase.get(subject_name[-1], '')
        # for i in data.keys():
            # print(data[i])
        #     print(data[i]["chapter_name"])
        #     print(data[i]["class"])
        #     print(data[i]["desc"])
        #     print(data[i]["upload_date"])

        self.subject_details = [
                {'text': f"{str(x)} {data[x]['class']}", 'chapter_name': data[x]['chapter_name'], 'upload_date': data[x]["upload_date"],
                 'link': data[x]['data_link']} for x in data.keys()]


class ForthWindow(Screen):
    pass


class FifthWindow(Screen):
    def on_pre_enter(self):
        with open("java_j.txt", 'r') as f:
            java = f.read()
            self.ids.java.text = str(java)


class SixthWindow(Screen):
    # new_name = ObjectProperty(None)
    # new_passw = ObjectProperty(None)

    def save_user_data(self, new_name, new_class, new_email, new_passw):
        from firebase import firebase
        firebase_data = firebase.FirebaseApplication('https://classmate-classes-default-rtdb.firebaseio.com/', None)
        data = {
            'Name': new_name.text,
            'Class': new_class.text,
            'Email': new_email.text,
            'Password': new_passw.text,
        }

        firebase_data.post('classmate-classes-default-rtdb/User', data)


class SeventhWindow(Screen):
    profile = "C:/Users/user/Downloads/rahul.jpg"


class EighthWindow(Screen):
    pass


class EachChapterButton(Button):
    def on_release(self):
        sm = App.get_running_app().root.ids.sm
        sm.get_screen('Ninth').ids.chapter_index.text = self.text
        sm.get_screen('Ninth').ids.chapter_name.text = self.chapter_name
        sm.get_screen('Ninth').ids.chapter_upload_date.text = f"{self.upload_date} on uploaded"
        sm.get_screen('Ninth').ids.pdfimage.text = self.link
        sm.current = 'Ninth'


class NinthWindow(Screen):
    def viewpdfimage(self, link):
        global image_link
        image_link.append(link)
        sm = App.get_running_app().root.ids.sm
        # sm.get_screen('Tenth').ids.image = link
        sm.current = 'Tenth'


class TenthWindow(Screen):
    image_source = StringProperty()

    def on_pre_enter(self):
        global image_link
        self.image_source = str(image_link[0])
        image_link.pop(0)


class SearchWindow(Screen):
    def wiki(self, quarry):
        if quarry != "":
            try:
                results = wikipedia.summary(quarry, auto_suggest=False)

            except wikipedia.WikipediaException as e:
                self.ids.result.text = str(f'Ask me like this!\n{e}')

            else:
                self.ids.result.text = str(results)


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
        Window.clearcolor = "teal"  # '#6B158A'
        Window.size = [300, 620]
        self.title = 'Classmate classes'
        return kv

    # def on_start(self):
    #     self.root.dispatch('on_enter')


subhi = MiniApp()
subhi.run()
