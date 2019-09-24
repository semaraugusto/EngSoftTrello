import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
from estorias import Estoria
import random
import banco

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #self.frames["InitialPage"] = InitialPage(container, self)
        #self.frames["InitialPage"].grid(row=0, column=0, sticky="nsew")

        #self.show_frame("InitialPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

app = Application()
app.geometry("800x600")
app.mainloop()