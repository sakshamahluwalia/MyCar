from view import Gauge
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.properties import BoundedNumericProperty

class GaugeApp(App):
    increasing = NumericProperty(1)
    begin = NumericProperty(50)
    step = NumericProperty(1)

    def build(self):
        box = BoxLayout(orientation='horizontal', padding=5)
        self.gauge = Gauge(value=50, size_gauge=256, size_text=25)
        self.speedgauge = Gauge(value=50, size_gauge=256, size_text=25)
        self.throttlegauge = Gauge(value=50, size_gauge=256, size_text=25)

        self.slider = Slider(orientation='vertical')

        # stepper = Slider(min=1, max=25)
        # stepper.bind(
        #     value=lambda instance, value: setattr(self, 'step', value)
        # )

        box.add_widget(self.gauge)
        box.add_widget(self.speedgauge)
        box.add_widget(self.throttlegauge)
        # box.add_widget(stepper)
        # box.add_widget(self.slider)
        Clock.schedule_interval(lambda *t: self.gauge_increment(self.gauge), 0.03)
        Clock.schedule_interval(lambda *t: self.gauge_increment(self.speedgauge), 0.03)
        Clock.schedule_interval(lambda *t: self.gauge_increment(self.throttlegauge), 0.03)
        return box

    def gauge_increment(self, gauge):
        begin = self.begin
        begin += self.step * self.increasing
        if begin > 0 and begin < 100:
            gauge.value = begin
        else:
            self.increasing *= -1
        self.begin = begin

if __name__ == '__main__':
    GaugeApp().run()
