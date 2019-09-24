import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
#from estorias import Estoria
import random
#import banco

class SampleApp(tk.Tk):

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
        self.frames["InitialPage"] = InitialPage(container, self)
        self.frames["InitialPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("InitialPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class InitialPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.projects = ["AEDSII-TP1", "COMPILADORESI-TP2", "ENGSOFT-TP3", "OCII-TP0"]
        self.initial_page_options = ["Create new project", "Delete project", "Configure project"]
        self.fontePadrao = ("Arial", "10")


        label = tk.Label(self, font=controller.title_font, pady=1)
        label.pack(fill="x")

        
        for i in range(0,len(self.initial_page_options)):
            brightness = 1
            bg_colour = "#0A6450"
            option = tk.Button(controller, text=self.initial_page_options[i], fg='White' if brightness < 120 else 'Black', bg=bg_colour)
            option.place(x = 20, y = 30 + i*50, width=120, height=30)

        self.projects_list_box = tk.Listbox(controller, width=70, height=35, selectmode=tk.BROWSE)
        for i in range(0, len(self.projects)):
            self.projects_list_box.insert(i, self.projects[i])
        self.projects_list_box.place(x=200, y=30)

        #banco.inicializaBanco()
        #self.estorias = []
        #self.carregaEstorias()

    #def carregaEstorias(self):
    #    command = "SELECT * FROM estorias;"
    #    result = banco.executeQuery(command)

    #    for linha in result:
    #        self.estorias.append(Estoria(linha[1], linha[2], linha[3], linha[0]))


    #def printEstorias(self):
    #    for estoria in self.estorias:
    #        print(str(estoria.id) + ", " + estoria.nome + ", " + estoria.descricao + ", " + str(estoria.story_points))

  
app = SampleApp()
app.geometry("800x600")
app.mainloop()