# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
#
#
# class HomeSubjects(GridLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def forthWB(self):
#         sm = App.get_running_app().root.ids.sm
#         sm.current = "Forth"
#
#     def thirdWB(self, subject):
#         sm = App.get_running_app().root.ids.sm
#         sm.get_screen('Third').ids.nav_name.text = f"{subject}         "
#         sm.current = "Third"
