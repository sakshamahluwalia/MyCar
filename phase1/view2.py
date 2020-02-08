import obd
import time
import random
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar



"""
This DashBoard will contain:
1. RPM: ProgressBar -> Gauge
2. Speed: ProgressBar -> Gauge
3. Throttle: ProgressBar -> Gauge
"""
# class DashBoard(GridLayout):
class DashBoard(BoxLayout):

    def __init__(self, **kwargs):
        super(DashBoard, self).__init__(**kwargs)
        # self.cols = 3
        self.orientation = 'vertical'
        self.rpm = self.pbar()
        self.add_widget(self.rpm)
        self.speed = self.pbar()
        self.add_widget(self.speed)
        self.throttle = self.pbar()
        self.add_widget(self.throttle)
        # self.add_widget(Label(text='User Name'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)

    def pbar(self):
        return ProgressBar(max=8000)

    def getrpm(self):
        return self.rpm

    def getspeed(self):
        return self.speed

    def getthrottle(self):
        return self.throttle

class MyApp(App):

    def build(self):
        self.root = DashBoard()
        Clock.schedule_interval(self.update, 0.5)
        return self.root

    def update(self, args):
        rpm = self.root.getrpm()
        speed = self.root.getspeed()
        throttle = self.root.getthrottle()

        rpm.value = random.randint(1, 8) * 1000
        speed.value = random.randint(1, 8) * 1000
        throttle.value = random.randint(1, 8) * 1000

if __name__ == '__main__':
    MyApp().run()
    # MyApp().update()
