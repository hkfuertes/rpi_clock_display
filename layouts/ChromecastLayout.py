from tkinter import *
from tkinter import ttk
from datetime import datetime
import tkinter.font as font
from widgets import WeatherFrame, ClockFrame, LocationFrame, IPFrame, ChromecastIndicatorFrame
from layouts.WeatherInfoLayout import WeatherInfoLayout
import pyowm, pychromecast
from config import Config
import fontawesome as fa


class ChromecastLayout(Frame):

    def get_chromecast(self, cast_name):
        chromecasts = pychromecast.get_chromecasts()
        [cc.device.friendly_name for cc in chromecasts]

        cast = next(cc for cc in chromecasts if cc.device.friendly_name == cast_name)
        # Start worker thread and wait for cast device to be ready
        cast.wait()

        return cast

    def listen_chromecast_status(self):
        if not self.cast.media_controller.status.player_is_idle:
            artist = self.cast.media_controller.status.artist
            title = self.cast.media_controller.status.title
            if self.title.get() != title:
                self.title.set(title)
                self.artist.set(artist)
                #print("[{} - {}]".format(title, artist))
            #self.progress['value'] = self.cast.media_controller.status.current_time
            #self.progress["maximum"] = self.cast.media_controller.status.duration
            #print("{} {}".format(self.cast.media_controller.status.current_time, self.cast.media_controller.status.duration))

        self.after(1000, self.listen_chromecast_status)

    def next_song(self, event):
        self.cast.media_controller.queue_next()

    def prev_song(self, event):
        self.cast.media_controller.queue_prev()

    def play_pause(self, event):
        if self.cast.media_controller.status.player_is_playing:
            self.play_icon.set(fa.icons["play"])
            self.cast.media_controller.pause()
        else:
            self.play_icon.set(fa.icons["pause"])
            self.cast.media_controller.play()

    def close_window(self, event):
        self.master.destroy()

    def __init__(self, arg_master, **options):
        self.cast = options.pop('caster', None)
        super(ChromecastLayout, self).__init__(arg_master, **options)
        self.configure(background='black', width=480, height=320)

        config = Config.getInstance()
        if self.cast is None:
            self.cast = self.get_chromecast(config['chromecast'])
        
        ci = Frame(self, bg="black")
        ci.grid(column=0, row=0, sticky=W, padx=10, pady=10)

        back = Label(ci, text=fa.icons["angle-left"], font=(config['fonts']['fa_solid'], 16), fg="white", bg="black")
        back.bind("<Button-1>", self.close_window)
        back.pack(side=LEFT, padx=10)

        canvas = Label(ci, text=fa.icons["chromecast"], font=(config['fonts']['fa_brands'], 16), fg="gray", bg="black")  
        canvas.pack(side=LEFT)
            
        location = Label(ci, text=config['chromecast'], font="Arial 16", fg="lightgray", bg="black")
        location.pack(side=LEFT)
        
        
        self.title = StringVar()
        self.title.set("<titulo_de_la_cancion>")
        title = Label(self, textvariable=self.title, font="Arial 24 bold", fg="lightgray", bg="black", anchor="w", justify=LEFT)
        title.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        self.artist = StringVar()
        self.artist.set("<artista_de_la_cancion>")
        artist = Label(self, textvariable=self.artist, font="Arial 16 italic", fg="lightgray",bg="black", anchor="w", justify=LEFT)
        artist.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        #self.progress = ttk.Progressbar(self, orient="horizontal",length=100, mode="determinate")
        #self.progress.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        b_f = Frame(self)
        b_f.configure(bg="black")
        b_f.grid(row=3, column=0, columnspan=2, sticky="w", padx=32, pady=32)

        icon_size = 48
        prev = Label(b_f, text=fa.icons["step-backward"], font=(config['fonts']['fa_solid'], icon_size), fg="white", bg="black")  
        prev.bind("<Button-1>", self.prev_song)
        prev.grid(row=1, column=0, padx=32, pady=32)

        self.play_icon = StringVar()
        self.play_icon.set(fa.icons["pause"])
        play = Label(b_f, textvariable=self.play_icon, font=(config['fonts']['fa_solid'], icon_size), fg="white", bg="black")  
        play.bind("<Button-1>", self.play_pause)
        play.grid(row=1, column=1, padx=32, pady=32)

        nxt = Label(b_f, text=fa.icons["step-forward"], font=(config['fonts']['fa_solid'], icon_size), fg="white", bg="black")  
        nxt.bind("<Button-1>", self.next_song)
        nxt.grid(row=1, column=2, padx=32, pady=32)
        

        self.listen_chromecast_status()

