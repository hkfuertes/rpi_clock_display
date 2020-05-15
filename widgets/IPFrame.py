from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
from datetime import datetime
from PIL import ImageTk,Image
import fontawesome as fa
import pyglet, os, socket


class IPFrame(Frame):
    def __init__(self, arg_master, **options):
        super(IPFrame, self).__init__(arg_master, **options)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.ip = s.getsockname()[0]
        s.close()
        
        self.configure(background="black")

        canvas = Label(self, text=fa.icons["wifi"], font=("Font Awesome 5 Free Solid", 12), fg="gray", bg="black")  
        canvas.pack(side=LEFT)

        location = Label(self, text=self.ip.upper(), font="Arial 12", fg="gray", bg="black")
        location.pack(side=LEFT)
