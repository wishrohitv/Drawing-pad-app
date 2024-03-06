from turtle import pos, width
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from sqlalchemy import values


class CanvasScreen(BoxLayout):
    def __init__(self, **kw):
        super(CanvasScreen, self).__init__(**kw)
        self.prev_touch_pos = None
        self.selected_colors = 0,0,0,1
        self.pencil_width_ = 2
        # line box
        with self.canvas:
            Color(rgba=(1,1,0,1))
            Line(width=1.2, rounded_rectangle=(self.x, self.y, self.width, self.height, 6))


    def on_touch_down(self, touch):
            self.prev_touch_pos = touch.pos
            with self.canvas:
                # r,g,b = random.randint(0,1), random.randint(0,1), random.randint(0,1)
                # if r and g and b == 1:
                #     r,g,b = 0, 1, 1
                Color(rgba = self.selected_colors)
                Line(width=self.pencil_width_, points=(touch.pos, touch.pos))

    def on_touch_move(self, touch):
        if self.prev_touch_pos:
            with self.canvas:
                # Color(rgba = self.selected_colors)
                # Line(width=2, points=(self.prev_touch_pos[0], self.prev_touch_pos[1], touch.x, touch.y))
                Line(width=self.pencil_width_, points=(self.prev_touch_pos[0], self.prev_touch_pos[1], touch.x, touch.y))
        self.prev_touch_pos = touch.pos

    def on_touch_up(self, touch):
        self.prev_touch_pos = None

    def clear_colors(self):
        self.canvas.clear()

class ScreenWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.canvas_screen = CanvasScreen()   
        # color picker
        self.color_picker = ColorPicker(color = (0,0,0,1))
        self.color_picker.bind(color=self.on_color)

        # color_pallete
        self.color_pallate = Popup(title="pick color", title_align="center", content=self.color_picker, size_hint=(.7,.7))

        # sider
        self.slider = Slider(value_track=True, step=.1, min=.1, max=10, value=2)
        self.slider.bind(value=self.pencil_width)
        self.slider_label = Label(color="black", size_hint=(.2, 1), font_size=18, text="2")
        
        # control buttons

        color_ = BoxLayout(padding=5, spacing=10, size_hint=(1,None), height=self.height)
        colors = ["red", "green", "yellow", "black", "pink", "blue"]

        for color in colors:
            color_.add_widget(ColoredBorderButton(text=f"{color}", pos_hint={'top':1}, group="colors", on_press=self.choosed_colors, background_normal="", background_color=color))

        # 2nd row
        slid_box = BoxLayout(size_hint=(1,None), height=40, padding=10)
    
        slid_box.add_widget(Button(text="clear", size_hint=(None,1), width=70, on_press=self.clear))
        # color _picker Button
        self.color_picker_button = Button(text="pick\ncolor", size_hint=(None,1), width=70, font_size=14,background_normal="", background_color="black", on_press=self.open_color_pallete)
        slid_box.add_widget(self.color_picker_button)
        slid_box.add_widget(self.slider)
        slid_box.add_widget(self.slider_label)

        # canvas screen

        # root box
        self.root_box = BoxLayout(orientation="vertical", padding=10)
        self.root_box.add_widget(color_)
        self.root_box.add_widget(slid_box)
        self.root_box.add_widget(self.canvas_screen)

        self.add_widget(self.root_box)


    def choosed_colors(self, instance):
        match instance.text:
            case "red":
                self.canvas_screen.selected_colors = 1,0,0,1
            case "green":
                self.canvas_screen.selected_colors = 0,1,0,1
            case "yellow":
                self.canvas_screen.selected_colors = 1,1,0,1
            case "black":
                self.canvas_screen.selected_colors = 0,0,0,1
            case "pink":
                self.canvas_screen.selected_colors = 1,0,1,1
            case "blue":
                self.canvas_screen.selected_colors = 0,0,1,1
                

    def clear(self, args):
        self.canvas_screen.clear_colors()

    def open_color_pallete(self, args):
        self.color_pallate.open()
        
    def on_color(self, instance, value):
        self.canvas_screen.selected_colors = tuple(value)
        self.color_picker_button.background_color = value
        self.color_pallate.dismiss()

    def pencil_width(self, instance, value):
        self.canvas_screen.pencil_width_ = value
        self.slider_label.text = str(round(value, 1))

class ColoredBorderButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint=(1,None)
        self.height=40

        # with self.canvas.before:
        #     Color(0,0,0,1)
        #     Line(width=4, rectangle=(self.x, self.y, self.width, self.height))

class Main(App):
    def build(self):
        Window.clearcolor = [1, 1, 1, 1]
        return ScreenWindow()
    
Main().run()
