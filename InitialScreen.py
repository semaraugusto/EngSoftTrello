import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
import random
from banco import *

class InitialPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.user_id = 0

        # Initializing Main label in the frame
        label = tk.Label(self, width=800, height=600)
        label.pack(pady=10,padx=10)

        # getting the projects avaiable
        self.projects = executeQuery("SELECT nome FROM projetos;")

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

    # function that create the buttons options
    def createOption(self, widget, option_string, function):
        option = tk.Button(widget, text=option_string, command=function, fg=self.options_brightness , bg=self.options_colour)
        option.place(x = 20, y = 30 + self.options_count*50, width=120, height=30)
        self.options_count += 1

    # get the new project data given by the user, and 
    def getSubmitedProject(self, widget, name_entry):
        name = name_entry.get()

        if name != "":
            insertProjeto(name)
            self.projects_list_box.insert(self.projects_list_box.size(), [name])
            name_entry.destroy()
            widget.destroy()
        else:
            # popup an error message and keeps the window open
            Errorlabel = tk.Label(widget, text="Name or description not given", background="red", fg="white")
            Errorlabel.grid(row=2,column=0)

    def cancelSubmitedProject(self, widget, name_entry):
        name_entry.destroy()
        widget.destroy()

    # Create the new project window popup to get the new project data
    def createNewProject(self):
        win = tk.Toplevel()
        win.wm_title("Window")

        label= tk.Label(win, text="Project Name",font=10)
        label.grid(row=0)
        name_entry = tk.Entry(win)
        name_entry.grid(row=0, column=1)

        submit_button = tk.Button(win, text="Submit", command= lambda: self.getSubmitedProject(win, name_entry))
        submit_button.grid(row=2, column=1)

        submit_button = tk.Button(win, text="Cancel", command= lambda: self.cancelSubmitedProject(win, name_entry))
        submit_button.grid(row=2, column=2)

    def deleteYesButton(self, widget, project_selected):
        for i in range(self.projects_list_box.size()):
            if(self.projects_list_box.get(i)[0] == project_selected[0]):
                self.projects_list_box.delete(i)
                break
        project_id = getById("projetos", project_selected[0])[0][0]
        deleteByID("projetos", project_id)
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

    def set_user_id(self, user_id):
        self.user_id = user_id