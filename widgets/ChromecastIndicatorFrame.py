from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
from datetime import datetime
from PIL import ImageTk,Image
import fontawesome as fa
import pyglet, os, time, pychromecast, threading
from config import Config
from layouts import ChromecastLayout
from windows import FullScreenWindow

class ChromecastIndicatorFrame(Frame):

    def paint_playing(self):
        self.canvas.configure(fg="lightgray")
        self.name.set(self.config['chromecast'].upper())

    def paint_idle(self):
        self.canvas.configure(fg="gray")
        self.name.set('')

    def get_chromecast(self):
        chromecasts = pychromecast.get_chromecasts()
        [cc.device.friendly_name for cc in chromecasts]

        cast = next(cc for cc in chromecasts if cc.device.friendly_name == self.config['chromecast'])
        # Start worker thread and wait for cast device to be ready
        cast.wait()

        return cast

    def listen_chromecast_status(self):
        #while not self.stop_chromecast_service:
        if self.cast.media_controller.status.player_is_idle:
            self.paint_idle()
        else:
            self.paint_playing()
        self.playing = not self.cast.media_controller.status.player_is_idle

        if self.playing:
            artist = self.cast.media_controller.status.artist
            title = self.cast.media_controller.status.title
            if self.title != title:
                self.title = title
                self.artist = artist
                print("[{} - {}]".format(title, artist))

        self.after(1000, self.listen_chromecast_status)

    def chromecast_window(self, event):
        print("[+] Opening Chromecast!")
        ww = FullScreenWindow(self.master)
        ww.configure(bg="black")
        wip = ChromecastLayout.ChromecastLayout(ww, caster=self.cast)
        wip.pack()

    def __init__(self, arg_master, **options):
        super(ChromecastIndicatorFrame, self).__init__(arg_master, **options)
        
        self.configure(background="black")

        self.config = Config.getInstance()
        self.name = StringVar()

        self.stop_chromecast_service = False
        self.playing = False
        self.title = ""
        self.artist = ""

        self.cast = self.get_chromecast()

        self.bind("<Button-1>", self.chromecast_window)

        self.canvas = Label(self, text=fa.icons["chromecast"], font=(self.config['fonts']['fa_brands'], 16), fg="gray", bg="black")  
        self.canvas.bind("<Button-1>", self.chromecast_window)
        self.canvas.pack(side=LEFT)
            
        #location = Label(self, textvariable=self.name, font="Arial 16", fg="lightgray", bg="black")
        #location.pack(side=LEFT)

        self.listen_chromecast_status()


        
