from tkinter import Tk, Toplevel

class FullscreenWindow(Toplevel):
    def __init__(self, *arg_master, **options):
        super(FullscreenWindow, self).__init__(*arg_master, **options)

        self.geometry("480x320")
        self.resizable(0, 0)

        self.state = True
        self.configure(cursor="none")
        self.attributes("-fullscreen", self.state)
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.attributes("-fullscreen", False)
        return "break"

