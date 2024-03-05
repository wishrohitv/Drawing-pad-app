from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider


class CanvasScreen(BoxLayout):
    def __init__(self, **kw):
        super(CanvasScreen, self).__init__(**kw)
        self.prev_touch_pos = None
        self.selected_colors = 0,0,0,1
        self.pencil_width_ = 2


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
                Line(width=2, points=(self.prev_touch_pos[0], self.prev_touch_pos[1], touch.x, touch.y))
        self.prev_touch_pos = touch.pos

    def on_touch_up(self, touch):
        self.prev_touch_pos = None

    def clear_colors(self):
        self.canvas.clear()

class ScreenWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        # color picker
        self.color_picker = ColorPicker()
        self.color_picker.bind(color=self.on_color)

        # color_pallete
        self.color_pallate = Popup(title="pick color", title_align="center", content=self.color_picker, size_hint=(.7,.7))

        # sider
        self.slider = Slider(value_track=True, step=.1, min=.1, max=10)
        self.slider.bind(value=self.pencil_width)

        # canvas screen
        self.canvas_screen = CanvasScreen()   
        self.add_widget(self.canvas_screen)
        
        float = BoxLayout(padding=5, spacing=10)
        float.add_widget(Button(text="clear", size_hint=(1,None), height=40, pos_hint={'top':1}, on_press=self.clear))
        self.add_widget(float)

        # color _picker Button
        self.color_picker_button = Button(text="pick\ncolor", size_hint=(1,None), height=40, pos_hint={'top':1},background_normal="", background_color="black", on_press=self.open_color_pallete)

        float.add_widget(self.color_picker_button)

        colors = ["red", "green", "yellow", "black", "pink", "blue"]

        for color in colors:
            float.add_widget(ColoredBorderButton(text=f"{color}", pos_hint={'top':1}, group="colors", on_press=self.choosed_colors, background_normal="", background_color=color))

        slid_box = BoxLayout(size_hint=(1,None), height="40dp")
        slid_box.add_widget(self.slider)
        self.add_widget(slid_box)

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
        print(value)
        self.canvas_screen.pencil_width_ = value

class ColoredBorderButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint=(1,None)
        self.height=40
        self.pos_hint= {'top':1}

        # with self.canvas.before:
        #     Color(0,0,0,1)
        #     Line(width=4, rectangle=(self.x, self.y, self.width, self.height))

class Main(App):
    def build(self):
        Window.clearcolor = [1, 1, 1, 1]
        return ScreenWindow()
    
Main().run()
