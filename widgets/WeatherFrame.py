from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
import pyowm

class WeatherFrame(Frame):

    def update_weather(self):
        w = self.observation.get_weather()
        status = w.get_detailed_status().upper()
        temp = round(w.get_temperature('celsius')['temp'])
        self._temp_text.set("{}º".format(temp))
        self._weather_text.set("{}".format(status))
        self.after(15*60*1000, self.update_weather)

    def __init__(self, arg_master, **options):
        location = "Pamplona"
        super(WeatherFrame, self).__init__(arg_master, **options)

        self.configure(background='black')

        owm = pyowm.OWM('966f9979caf0bf53ff0706a981c17d49')
        self.observation = owm.weather_at_place(location+",ES")

        self._temp_text = StringVar()
        self._weather_text = StringVar()

        temp = Label(self, textvariable = self._temp_text, font="Arial 16 bold", fg="gray", bg="black")
        temp.pack(side=LEFT)

        weather = Label(self, textvariable = self._weather_text, font="Arial 16", fg="gray", bg="black")
        weather.pack(side=LEFT, padx=(8,0))

        self.update_weather()