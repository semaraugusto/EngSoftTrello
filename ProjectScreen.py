import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
import random
from banco import *

class ProjectPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.project_name = "Project Name"
        label = tk.Label(self, text=self.project_name, font=("Verdana", 12))
        label.grid(row=0, column=0, columnspan=8, rowspan=3)

        stories = []
        tasks = []
        print(tasks)
        doing = []
        done = []
        for t in tasks:
            if t[6]:
                done.append(t)
            else:
                doing.append(t)

        self.list_boxes = {}

        self.createListBox(self, stories, "Stories", 3, 0, "E{}: ")
        self.createListBox(self, tasks, "Tasks", 3, 2, "T{}: ", add=False, remove=True)
        self.createListBox(self, doing, "Doing", 3, 4, "T{}: ", add=False, remove=True)
        self.createListBox(self, done, "Done", 3, 6, "T{}: ", add=False, remove=True)

        back_to_home_button = tk.Button(self, text="Back to home", command= lambda: controller.show_initialframe(0))
        back_to_home_button.grid(row=6, column=0, columnspan=6)
        
    def createListBox(self, widged, array, list_name, r, c, prefix, add=True, remove=True):
        array_label = tk.Label(widged, text=list_name)
        array_label.grid(row=r, column=c, columnspan=2)
        array_list = tk.Listbox(widged, width=23, height=30)
        for i in range(len(array)):
            if list_name == "Stories":
                array_list.insert(i, prefix.format(i) + array[i][1])
            elif list_name == "Tasks" or list_name == "Done" or list_name == "Doing":
                array_list.insert(i, prefix.format(i) + array[i][3])

        array_list.grid(row=r+1, column=c, columnspan=2)
        
        add_button = None
        remove_button = None

        if add:
            add_button = tk.Button(widged, text="Add", width=4, command= lambda: self.createNewProject(list_name))
            add_button.grid(row=r+2, column=c)

        if remove:
            remove_button = tk.Button(widged, text="Remove", width=4, command= lambda: self.deleteProject(list_name))
            remove_button.grid(row=r+2, column=c+1)

        self.list_boxes[list_name] = [array_label, array_list, add_button, remove_button]

    def defineProjectName(self, project_name):
        self.project_name = project_name

    # get the new project data given by the user, and 
    def getSubmited(self, widget, name_entry, description_entry):
        name = name_entry.get()
        description = description_entry.get()
        if name != "":
            stories = selectAll("estorias")
            self.list_boxes["Stories"].insert(len(stories) - 1, name)
            insertEstoria(name, description, 0)
            name_entry.destroy()
            widget.destroy()
        else:
            # popup an error message and keeps the window open
            Errorlabel = tk.Label(widget, text="description not given", background="red", fg="white")
            Errorlabel.grid(row=2,column=0)

    def cancelSubmited(self, widget, name_entry, description_entry):
        name_entry.destroy()
        description_entry.destroy()
        widget.destroy()

    # Create the new project window popup to get the new project data
    def createNewProject(self, list_selected):
        win = tk.Toplevel()
        win.wm_title("Window")


        label= tk.Label(win, text=list_selected + ":",font=10)
        label.grid(row=0)
        name_entry = tk.Entry(win)
        description_entry = tk.Entry(win)
        name_entry.grid(row=0, column=1)

        submit_button = tk.Button(win, text="Submit", command= lambda: self.getSubmited(win, name_entry, description_entry))
        submit_button.grid(row=1, column=0)

        submit_button = tk.Button(win, text="Cancel", command= lambda: self.cancelSubmited(win, name_entry, description_entry))
        submit_button.grid(row=1, column=1)

    def deleteYesButton(self, widget, project_selected):
        # deleteProjectInDataBase()
        # updateInterfaceData()
        widget.destroy()

    def deleteNoButton(self, widget):
        widget.destroy()

    # Create the delete project window popup
    def deleteProject(self, list_selected):
        win = tk.Toplevel()
        win.wm_title("Window")

        project_selected = self.list_boxes[list_selected][1].get(tk.ACTIVE)
        label= tk.Label(win, text="Are you sure you want to delete '{}' ?".format(project_selected),font=10)
        label.grid(row=0)

        yes_button = tk.Button(win, text="yes", command= lambda: self.deleteYesButton(win, project_selected))
        yes_button.grid(row=4, column=1)

        no_button = tk.Button(win, text="no", command= lambda: self.deleteNoButton(win))
        no_button.grid(row=4, column=2)
        