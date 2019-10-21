import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
import random
from banco import *
from InitialScreen import InitialPage
from ProjectScreen import ProjectPage
from LoginScreen import LoginPage

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in [LoginPage ,InitialPage, ProjectPage]:
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_initialframe(self, user_id):
        frame = self.frames[InitialPage]
        frame.set_user_id(user_id)
        frame.loadProjects(self)
        frame.tkraise()

    def show_projectFrame(self, project_name):
        print(project_name, )
        project_id = getById("projetos", project_name[0])
        frame = self.frames[ProjectPage]
        print(project_name, project_id)
        frame.initializeProject(self, project_id[0][0], project_name[0])
        frame.tkraise()


app = Application()
app.geometry("850x600")
app.mainloop()
