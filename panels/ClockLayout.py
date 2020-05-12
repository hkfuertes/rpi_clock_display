from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
from threading import Thread
from time import sleep
from datetime import datetime
import pyowm


class ClockLayout(Frame):

    def update_clock(self):
        if self.tick :
            self._clock_text.set(datetime.now().strftime('%H:%M'))
        else:
            self._clock_text.set(datetime.now().strftime('%H %M'))
        self._date_text.set(datetime.now().strftime('%A %d %B'))
        self.tick = not self.tick
        self.after(1000, self.update_clock)

    def update_weather(self):
        w = self.observation.get_weather()
        self._weather_text.set("{}º".format(round(w.get_temperature('celsius')['temp'])))
        self.after(15*60*1000, self.update_weather)

    def __init__(self, arg_master, **options):
        super(ClockLayout, self).__init__(arg_master, **options)

        self.tick = True

        self.configure(background='black')

        owm = pyowm.OWM('966f9979caf0bf53ff0706a981c17d49')
        location="Pamplona"
        self.observation = owm.weather_at_place(location+",ES")

        self._weather_text = StringVar()
        self._clock_text = StringVar()
        #self._clock_text.set(datetime.now().strftime('%H:%M:%S'))
        self._clock_text.set(datetime.now().strftime('%H:%M'))
        self._date_text = StringVar()
        self._date_text.set(datetime.now().strftime('%A %d %B'))


        weather = Label(self, textvariable = self._weather_text, font="Arial 24 bold", fg="gray", bg="black")
        weather.grid(row=0, column=0, sticky="w")

        location = Label(self, text=location, font="Arial 24", fg="gray", bg="black")
        location.grid(row=0, column=1, sticky="e")

        clock = Label(self, textvariable = self._clock_text, font="Arial 128", fg="white", bg="black")
        clock.grid(row=1, column=0, columnspan=2)

        date = Label(self, textvariable = self._date_text, font="Arial 24 italic", fg="gray", bg="black", anchor="e")
        date.grid(row=2, column=1, columnspan=2, sticky="e")

        self.update_clock()


        self.update_weather()
    
