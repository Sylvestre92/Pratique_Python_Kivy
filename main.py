from kivy.app import App
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        #print("INIT w: " + str(self.width) + " H: " + str(self.height))
        self.init_vertical_lines()


    def on_parent(self, widget, parent):
        #print("ON PARENT w: " + str(self.width) + " H:" + str(self.height))
        pass

    def on_size(self, *args):
        #print("INIT w: " + str(self.width) + " H: " + str(self.height))
        self.perspective_point_x = self.width/2
        self.perspective_point_y = self.height*0.75

    def on_perspective_point_x(self, widget, value):
        #print("PX: " + str(value))
        pass

    def on_perspective_point_y(self, widget, value):
        #print("PY: " + str(value))
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            Line(points=[100, 0, 100, 100])




class GalaxyApp(App):
    pass


GalaxyApp().run()
