from turtle import circle

from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class WidgetsExample(GridLayout):
    Count = 1
    count_enabled = BooleanProperty()
    My_text = StringProperty("1")
    #Slider_value_txt = StringProperty("value")

    def on_switch_active(self, widget):
        print("switch : "+ str(widget.active))


    def on_button_press(self):
        print("Count")
        if self.count_enabled:
            self.Count += 1
            self.My_text = str(self.Count)

    def on_toggle_button(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled =True
    def on_value_press(self, widget):
        print("value: "+ str(int(widget.value)))
        #self.Slider_value_txt = str(int(widget.value))


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation= "lr-bt"
        for i in range(0, 100):
            #size = dp(100)+i*10
            size=dp(100)
            b = Button(text= str(i+1), size_hint =(None, None), size=(size, size))
            self.add_widget(b)


#class GridLayoutExample(GridLayout):
    #pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
""" def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass
class CanvasExample3(Widget):
    pass
class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(1, 0, 0)
            Line(circle=(400, 200, 80), width=2)
            Color(0, 1, 0)
            Line(rectangle=(700, 500, 150, 100), width=2)
            self.rec=Rectangle(pos=(700, 200), size=(150, 150))
    def btn_cliked(self):
        #print
        x, y = self.rec.pos
        w, z = self.rec.size
        inc = dp(10)


        diff = self.width - (x+w)
        if diff <inc:
            inc = diff
        x += inc
        self.rec.pos=(x, y)

    class CanvasExample5(Widget):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.ball_size = dp(50)
            self.vx= dp(5)
            self.vy = dp(7)
            with self.canvas:
                self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            Clock.schedule_interval(self.update, 1/60)


        def on_size(self, *args):
            self.ball.pos = (self.center_x - self.ball_size/2, self.center_y-self.ball_size/2)

        def update(self, dt):
            x, y = self.ball.pos
            x += self.vx
            y += self.vy
            if y + self.ball_size > self.height:
                y = self.height - self.ball_size
                self.vy = -self.vy
            self.ball.pos=(x, y)

            if x + self.ball_size > self.width:
                x = self.width - self.ball_size
                self.vx = -self.vx
            if y < 0:
                y =0
                self.vy = -self.vy
            if x < 0:
                x =0
                self.vx = -self.vx

    class CanvasExample6(Widget):
        pass
    class CanvasExample7(BoxLayout):
        pass




TheLabApp().run()