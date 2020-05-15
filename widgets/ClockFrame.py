from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
from datetime import datetime
from config import Config

class ClockFrame(Frame):

    def update_clock(self):
        self._clock_h_text.set(datetime.now().strftime('%H'))
        self._clock_m_text.set(datetime.now().strftime('%M'))
        if self.tick :
            self.clock_dot.configure(fg="grey")
        else:
            self.clock_dot.configure(fg="white")
        self._date_text.set(datetime.now().strftime(self.cnf['date']['format']).upper())
        self.tick = not self.tick
        self.after(1000, self.update_clock)

    def __init__(self, arg_master, **options):
        super(ClockFrame, self).__init__(arg_master, **options)

        self.cnf = Config.getInstance()

        self.tick = True
        clock_size = 118

        self.configure(background='black')

        self._clock_m_text = StringVar()
        self._clock_h_text = StringVar()

        self._date_text = StringVar()

        cFrame = Frame(self)
        cFrame.pack(anchor="s")

        clock_h = Label(cFrame, textvariable = self._clock_h_text, font=("Arial", clock_size), fg="white", bg="black")
        clock_h.pack(side=LEFT)

        self.clock_dot = Label(cFrame, text = ":", font=("Arial", clock_size), fg="white", bg="black")
        self.clock_dot.pack(side=LEFT)

        clock_m = Label(cFrame, textvariable = self._clock_m_text, font=("Arial", clock_size), fg="white", bg="black")
        clock_m.pack(side=LEFT)

        date = Label(self, textvariable = self._date_text, font="Arial 16 italic", fg="gray", bg="black", anchor="e")
        date.pack(fill=X, anchor="n")

        self.update_clock()

