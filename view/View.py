__author__ = 'fx'

from tkinter import *

class View(Frame):

    def __init__(self, **kwargs):
        Frame.__init__(self, Tk(),**kwargs)
        self.pack(fill=BOTH)
        self.mCanvas = Canvas(self, width=400, height=300)