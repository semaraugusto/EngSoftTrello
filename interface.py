import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
#from estorias import Estoria
import random
#import banco

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in [InitialPage]:#, ProjectWindow, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(InitialPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def show_projectFrame(self, project_name):
        print(project_name)
        frame = self.frames[InitialPage]
        frame.defineProjectName(project_name)
        frame.tkraise()


class InitialPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        # Initializing Main label in the frame
        label = tk.Label(self, width=800, height=600)
        label.pack(pady=10,padx=10)

        # getting the projects avaiable
        self.projects = ["AEDSII-TP1", "COMPILADORESI-TP2", "ENGSOFT-TP3", "OCII-TP0"]

        # options visual configurations
        self.options_brightness = "White"
        self.options_colour = "#0A6450"
        self.options_count = 0

        # creating options avaiable
        self.createOption(self, "Create new project", self.createNewProject)
        self.createOption(self, "Delete project", self.deleteProject)

        # creating the list of projects that the user have
        self.projects_list_box = tk.Listbox(self, width=70, height=35, selectmode=tk.BROWSE)
        for i in range(0, len(self.projects)):
            self.projects_list_box.insert(i, self.projects[i])
        
        self.projects_list_box.bind("<Double-Button-1>", lambda x: controller.show_projectFrame(self.projects_list_box.get(tk.ACTIVE)))
        self.projects_list_box.place(x=200, y=30)

        #button2 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        #button2.place()

    # function that create the buttons options
    def createOption(self, widget, option_string, function):
        option = tk.Button(widget, text=option_string, command=function, fg=self.options_brightness , bg=self.options_colour)
        option.place(x = 20, y = 30 + self.options_count*50, width=120, height=30)
        self.options_count += 1

    # get the new project data given by the user, and 
    def getSubmited(self, widget, name_entry, description_entry):
        name = name_entry.get()
        description = description_entry.get()

        if name != "" and description != "":
            # addProjectInDataBase()
            # updateInterfaceData()
            name_entry.destroy()
            description_entry.destroy()
            widget.destroy()
        else:
            # popup an error message and keeps the window open
            Errorlabel = tk.Label(widget, text="Name or description not given", background="red", fg="white")
            Errorlabel.grid(row=2,column=0)

    def cancelSubmited(self, widget, name_entry, description_entry):
        name_entry.destroy()
        description_entry.destroy()
        widget.destroy()

    # Create the new project window popup to get the new project data
    def createNewProject(self):
        win = tk.Toplevel()
        win.wm_title("Window")

        label= tk.Label(win, text="Project Name",font=10)
        label.grid(row=0)
        name_entry = tk.Entry(win)
        name_entry.grid(row=0, column=1)


        label= tk.Label(win, text="Description", font=10)
        label.grid(row=1)
        description_entry = tk.Entry(win)
        description_entry.grid(row=1, column=1)

        submit_button = tk.Button(win, text="Submit", command= lambda: self.getSubmited(win, name_entry, description_entry))
        submit_button.grid(row=2, column=1)

        submit_button = tk.Button(win, text="Cancel", command= lambda: self.cancelSubmited(win, name_entry, description_entry))
        submit_button.grid(row=2, column=2)

    def deleteYesButton(self, widget, project_selected):
        # deleteProjectInDataBase()
        # updateInterfaceData()
        widget.destroy()

    def deleteNoButton(self, widget):
        widget.destroy()

    # Create the delete project window popup
    def deleteProject(self):
        win = tk.Toplevel()
        win.wm_title("Window")

        project_selected = self.projects_list_box.get(tk.ACTIVE)
        label= tk.Label(win, text="Are you sure you want to delete '{}' ?".format(project_selected),font=10)
        label.grid(row=0)

        yes_button = tk.Button(win, text="yes", command= lambda: self.deleteYesButton(win, project_selected))
        yes_button.grid(row=4, column=1)

        no_button = tk.Button(win, text="no", command= lambda: self.deleteNoButton(win))
        no_button.grid(row=4, column=2)
        
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

app = Application()
app.geometry("800x600")
app.mainloop()