from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT, Button
from datetime import datetime
from widgets import LocationFrame
from widgets.WeatherForecastFrame import WeatherForecastFrame
import pyowm


class WeatherInfoLayout(Frame):

    def setOWM(self, owm):
        fc = owm.daily_forecast(self.location)
        ws = fc.get_forecast().get_weathers()
        self.today.update_weather(ws[0])
        self.tomorow.update_weather(ws[1])
        self.after.update_weather(ws[2])

    def __init__(self, arg_master, **options):
        super(WeatherInfoLayout, self).__init__(arg_master, **options)

        self.configure(background='black')

        self.location="Pamplona, ES"

        close = Button(self, text="X")
        close.grid(row=0, column=1, sticky="e")

        weather = Frame(self)
        weather.grid(row=1, column=0, columnspan=2)

        self.today = WeatherForecastFrame(weather)
        self.today.grid(row=1, column=0)

        self.tomorow = WeatherForecastFrame(weather)
        self.tomorow.grid(row=1, column=1)

        self.after = WeatherForecastFrame(weather)
        self.after.grid(row=1, column=2)

        location = LocationFrame(self)
        location.grid(row=2, column=1, sticky="e")


