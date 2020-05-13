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
        status = w.get_detailed_status().upper()
        temp = round(w.get_temperature('celsius')['temp'])
        self._temp_text.set("{}º".format(temp))
        self._weather_text.set("{}".format(status))
        self.after(15*60*1000, self.update_weather)

    def __init__(self, arg_master, **options):
        super(ClockLayout, self).__init__(arg_master, **options)

        self.tick = True

        self.configure(background='black')

        owm = pyowm.OWM('966f9979caf0bf53ff0706a981c17d49')
        location="Pamplona"
        self.observation = owm.weather_at_place(location+",ES")

        self._temp_text = StringVar()
        self._weather_text = StringVar()
        self._clock_text = StringVar()
        #self._clock_text.set(datetime.now().strftime('%H:%M:%S'))
        self._clock_text.set(datetime.now().strftime('%H:%M'))
        self._date_text = StringVar()
        self._date_text.set(datetime.now().strftime('%A %d %B'))

        wFrame = Frame(self)
        wFrame.configure(background='black')
        wFrame.grid(row=0, column=0, columnspan=2, sticky="w")

        temp = Label(wFrame, textvariable = self._temp_text, font="Arial 16 bold", fg="gray", bg="black")
        temp.pack(side=LEFT)

        weather = Label(wFrame, textvariable = self._weather_text, font="Arial 16", fg="gray", bg="black")
        weather.pack(side=LEFT, padx=(8,0))

        location = Label(self, text=location.upper(), font="Arial 16", fg="gray", bg="black")
        location.grid(row=0, column=1, columnspan=2, sticky="e")

        clock = Label(self, textvariable = self._clock_text, font="Arial 128", fg="white", bg="black")
        clock.grid(row=1, column=0, columnspan=2)

        date = Label(self, textvariable = self._date_text, font="Arial 24 italic", fg="gray", bg="black", anchor="e")
        date.grid(row=2, column=1, columnspan=2, sticky="e")

        self.update_clock()


        self.update_weather()
    
