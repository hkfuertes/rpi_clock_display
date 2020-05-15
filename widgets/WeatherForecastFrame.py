from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
import pyowm, os, json

class WeatherForecastFrame(Frame):

    def load_icon_map(self):
        json_path = os.path.join(os.path.dirname(__file__), '../owfont-regular.maping.json')
        json1_file = open(json_path)
        json1_str = json1_file.read()
        return json.loads(json1_str)

    def update_weather(self, w):
        code = str(w.get_weather_code())
        char = int(self.map[code],0)
        temps = w.get_temperature('celsius')
        self._weather_icon.set("{}".format(chr(char)))
        self._temp_text.set("{}º/{}º".format(temps['max'], temps['min']))
        #self.after(15*60*1000, self.update_weather)

    def __init__(self, arg_master, **options):
        super(WeatherForecastFrame, self).__init__(arg_master, **options)

        self.configure(background='black')
        self.map = self.load_icon_map()

        self._temp_text = StringVar()
        self._weather_icon = StringVar()

        icon = Label(self, textvariable = self._weather_icon, font=("owf-regular",16), fg="lightgray", bg="black")
        icon.pack()

        temp = Label(self, textvariable = self._temp_text, font="Arial 16 bold", fg="lightgray", bg="black")
        temp.pack()