from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
from datetime import datetime
from PIL import ImageTk,Image
import fontawesome as fa
import pyglet, os, socket


class IPFrame(Frame):
    def __init__(self, arg_master, **options):
        super(IPFrame, self).__init__(arg_master, **options)
        
        self.configure(background="black")

        canvas = Label(self, text=fa.icons["wifi"], font=("Font Awesome 5 Free Solid", 12), fg="gray", bg="black")  
        canvas.pack(side=LEFT)

        self.location = socket.gethostbyname(socket.gethostname())
        location = Label(self, text=self.location.upper(), font="Arial 12", fg="gray", bg="black")
        location.pack(side=LEFT)
