from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
from datetime import datetime
from PIL import ImageTk,Image
import fontawesome as fa
import pyglet
import os

class LocationFrame(Frame):
    def __init__(self, arg_master, **options):
        super(LocationFrame, self).__init__(arg_master, **options)
        
        self.configure(background="black")

        canvas = Label(self, text=fa.icons["map-marker-alt"], font=("Font Awesome 5 Free Solid", 16), fg="gray", bg="black")  
        canvas.pack(side=LEFT)

        self.location = "Pamplona"
        location = Label(self, text=self.location.upper(), font="Arial 16", fg="gray", bg="black")
        location.pack(side=LEFT)
