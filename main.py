from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
import random


class CanvasScreen(BoxLayout):
    def __init__(self, **kw):
        super(CanvasScreen, self).__init__(**kw)
        self.prev_touch_pos = None
        self.selected_colors = 0,0,0,1 


    def on_touch_down(self, touch):
            self.prev_touch_pos = touch.pos
            with self.canvas:
                Color(rgba = self.selected_colors)
                Line(width=2, points=(touch.pos, touch.pos))

    def on_touch_move(self, touch):
        if self.prev_touch_pos:
            with self.canvas:
                Line(width=2, points=(self.prev_touch_pos[0], self.prev_touch_pos[1], touch.x, touch.y))
        self.prev_touch_pos = touch.pos

    def on_touch_up(self, touch):
        self.prev_touch_pos = None

    def clear_colors(self):
        self.canvas.clear()

class ScreenWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.canvas_screen = CanvasScreen()

        self.add_widget(self.canvas_screen)

        float = BoxLayout(padding=5, spacing=10)
        float.add_widget(Button(text="clear", size_hint=(1,None), height=40, pos_hint={'top':1}, on_press=self.clear))
        self.add_widget(float)

        colors = ["red", "green", "yellow", "black", "pink", "blue"]

        for color in colors:
            float.add_widget(ColoredBorderButton(text=f"{color}", pos_hint={'top':1}, group="colors", on_press=self.choosed_colors, background_normal="", background_color=color))

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

class ColoredBorderButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint=(1,None)
        self.height=40

        with self.canvas.before:
            Color(0,0,0,1)
            Line(width=4, rectangle=(self.x, self.y, self.width, self.height))

class Main(App):
    def build(self):
        Window.clearcolor = [1, 1, 1, 1]
        return ScreenWindow()
    
Main().run()
