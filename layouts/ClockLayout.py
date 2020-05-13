from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
from datetime import datetime
from widgets import WeatherFrame, ClockFrame, LocationFrame, IPFrame
import pyowm


class ClockLayout(Frame):

    def __init__(self, arg_master, **options):
        super(ClockLayout, self).__init__(arg_master, **options)

        self.configure(background='black')

        wFrame = WeatherFrame(self)
        wFrame.grid(row=0, column=0, sticky="w")

        clock = ClockFrame(self)
        clock.grid(row=1, column=0, columnspan=2)

        location = LocationFrame(self)
        location.grid(row=2, column=1, sticky="e")

        ip = IPFrame(self)
        ip.grid(row=2, column=0, sticky="w")

