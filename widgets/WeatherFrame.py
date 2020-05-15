from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT, Button, FLAT
from windows.FullScreenWindow import FullscreenWindow
from layouts.WeatherInfoLayout import WeatherInfoLayout
import pyowm, os, json

class WeatherFrame(Frame):

    def load_icon_map(self):
        json_path = os.path.join(os.path.dirname(__file__), '../owfont-regular.maping.json')
        json1_file = open(json_path)
        json1_str = json1_file.read()
        return json.loads(json1_str)

    def update_weather(self):
        w = self.observation.get_weather()
        status = w.get_detailed_status().upper()
        temp = round(w.get_temperature('celsius')['temp'])
        code = str(w.get_weather_code())
        char = int(self.map[code],0)
        self._weather_icon.set("{}".format(chr(char)))
        self._temp_text.set("{}º".format(temp))
        self._weather_text.set("{}".format(status))
        self.after(15*60*1000, self.update_weather)

    def weather_window(self, event):
        print("Weather Clicked!")
        ww = FullscreenWindow(self.master)
        ww.configure(bg="black")
        wip = WeatherInfoLayout(ww)
        wip.setOwm(self.owm)
        wip.pack()

    def __init__(self, arg_master, **options):
        location = "Pamplona"
        super(WeatherFrame, self).__init__(arg_master, **options)

        self.configure(background='black')
        self.map = self.load_icon_map()

        self.owm = pyowm.OWM('966f9979caf0bf53ff0706a981c17d49')
        self.observation = self.owm.weather_at_place(location+",ES")

        self._temp_text = StringVar()
        self._weather_text = StringVar()
        self._weather_icon = StringVar()

        icon = Label(self, textvariable = self._weather_icon, font=("owf-regular",24), fg="lightgray", bg="black")
        #icon.bind("<Button-1>", self.weather_window)
        #icon.configure(cursor="hand1")
        icon.pack(side=LEFT)

        temp = Label(self, textvariable = self._temp_text, font="Arial 16 bold", fg="lightgray", bg="black")
        temp.pack(side=LEFT)

        weather = Label(self, textvariable = self._weather_text, font="Arial 16", fg="lightgray", bg="black")
        weather.pack(side=LEFT, padx=(8,0))

        self.update_weather()