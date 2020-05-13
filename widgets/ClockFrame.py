from tkinter import Frame, Label, StringVar, CENTER, X, LEFT, RIGHT
from datetime import datetime

class ClockFrame(Frame):

    def update_clock(self):
        if self.tick :
            self._clock_text.set(datetime.now().strftime('%H:%M'))
        else:
            self._clock_text.set(datetime.now().strftime('%H %M'))
        self._date_text.set(datetime.now().strftime('%A %d %B'))
        self.tick = not self.tick
        self.after(1000, self.update_clock)

    def __init__(self, arg_master, **options):
        super(ClockFrame, self).__init__(arg_master, **options)

        self.tick = True

        self.configure(background='black')

        self._clock_text = StringVar()
        #self._clock_text.set(datetime.now().strftime('%H:%M:%S'))
        self._clock_text.set(datetime.now().strftime('%H:%M'))
        self._date_text = StringVar()
        self._date_text.set(datetime.now().strftime('%A %d %B'))

        clock = Label(self, textvariable = self._clock_text, font="Arial 128", fg="white", bg="black")
        clock.pack()

        date = Label(self, textvariable = self._date_text, font="Arial 24 italic", fg="gray", bg="black", anchor="e")
        date.pack(fill=X)

        self.update_clock()

