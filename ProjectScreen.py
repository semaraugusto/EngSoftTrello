import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
import random
from banco import *

class ProjectPage (tk.Frame):
    project_name = ""
    project_id = 0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def initializeProject(self, controller, project_id, project_name):
        label = tk.Label(self, text=project_name, font=("Verdana", 12))
        label.grid(row=0, column=0, columnspan=8, rowspan=3)
        self.project_id = project_id
        self.project_name = project_name

        stories = consultaEstoriasProjeto(self.project_id)
        print(stories)
        tasks = []
        for e in stories:
            task = consultaTarefasEstorias(e[0])
            if len(task) != 0:
                tasks += task
        doing = []
        done = []

        self.list_boxes = {}

        self.createListBox(self, stories, "Stories", 3, 0, "E{}: ")
        self.createListBox(self, tasks, "Tasks", 3, 2, "T{}: ", add=True, remove=True)
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
                array_list.insert(i, prefix.format(i) + array[i][2])
                array_list.bind("<Double-Button-1>",  lambda x: self.storyWindow(array_list.get(tk.ACTIVE), self.getStoryDescription(array_list.get(tk.ACTIVE)), self.getStoryPoints(array_list.get(tk.ACTIVE))))
            elif list_name == "Tasks" or list_name == "Done" or list_name == "Doing":
                print(i, prefix.format(i) ,array)
                array_list.insert(i, prefix.format(i) + array[i][2])

        array_list.grid(row=r+1, column=c, columnspan=2)
        
        add_button = None
        remove_button = None

        if add:
            if(list_name == "Stories"):
                add_button = tk.Button(widged, text="Add", width=6, command= lambda: self.createNewStory())
                add_button.grid(row=r+2, column=c)
            elif list_name == "Tasks" or list_name == "Done" or list_name == "Doing":
                add_button = tk.Button(widged, text="Add", width=6, command= lambda: self.createNewTask())
                add_button.grid(row=r+2, column=c)

        if remove:
            if(list_name == "Stories"):
                remove_button = tk.Button(widged, text="Remove", width=6, command= lambda: self.deleteStory())
                remove_button.grid(row=r+2, column=c+1)
            elif list_name == "Tasks" or list_name == "Done" or list_name == "Doing":
                remove_button = tk.Button(widged, text="Remove", width=6, command= lambda: self.deleteTask())
                remove_button.grid(row=r+2, column=c+1)

        self.list_boxes[list_name] = [array_label, array_list, add_button, remove_button]

    def defineProjectName(self, project_name):
        self.project_name = project_name

    def getStoryDescription(self, story_name):
        story_name = story_name[story_name.find(":")+2:]
        story_id = getById("estorias", story_name)
        story = selectAllbyID("estorias", story_id[0][0])
        return story[0][3]

    def getStoryPoints(self, story_name):
        story_name = story_name[story_name.find(":")+2:]
        story_id = getById("estorias", story_name)
        story = selectAllbyID("estorias", story_id[0][0])
        print(story)
        return story[0][4]

    # get the new story data given by the user, and 
    def getSubmitedStory(self, widget, name_entry, description_entry, sp_entry=None):
        name = name_entry.get()
        if sp_entry is not None:
            story_points = sp_entry.get()
        else:
            story_points = 0

        description = description_entry.get("1.0", tk.END)
        if name != "":
            list_box = self.list_boxes["Stories"][1]
            list_size = list_box.size() 
            list_box.insert(list_size, "E{}: ".format(list_size) + name)
            insertEstoria(self.project_id, name, description, story_points)
            name_entry.destroy()
            widget.destroy()
        else:
            # popup an error message and keeps the window open
            Errorlabel = tk.Label(widget, text="description not given", background="red", fg="white")
            Errorlabel.grid(row=2,column=0)

    def cancelSubmitedStory(self, widget, name_entry, description_entry, sp_entry=None):
        name_entry.destroy()
        description_entry.destroy()
        widget.destroy()
        if sp_entry is not None:
            sp_entry.destroy()


    # Create the new story window popup to get the new project data
    # def createNewStory(self):
    #     win = tk.Toplevel()
    #     win.wm_title("Window")
    #
    #     label= tk.Label(win, text="Story name: ", font=10)
    #     label.grid(row=0)
    #     name_entry = tk.Entry(win)
    #     name_entry.grid(row=0, column=1)
    #
    #     label = tk.Label(win, text="Description: ", font=10)
    #     label.grid(row=1)
    #     description_entry = tk.Text(win)
    #     description_entry.grid(row=1, column=1)
    #
    #     submit_button = tk.Button(win, text="Submit", command= lambda: self.getSubmitedStory(win, name_entry, description_entry))
    #     submit_button.grid(row=2, column=0)
    #
    #     submit_button = tk.Button(win, text="Cancel", command= lambda: self.cancelSubmitedStory(win, name_entry, description_entry))
    #     submit_button.grid(row=2, column=1)

    def createNewStory(self):
        win = tk.Toplevel()
        win.wm_title("Window")

        label = tk.Label(win, text="Story name: ", font=10)
        label.grid(row=0)
        name_entry = tk.Entry(win)
        name_entry.grid(row=0, column=1)

        label = tk.Label(win, text="Story points: ", font=10)
        label.grid(row=1)
        sp_entry = tk.Entry(win)
        sp_entry.grid(row=1, column=1)

        label = tk.Label(win, text="Description: ", font=10)
        label.grid(row=2)
        description_entry = tk.Text(win)
        description_entry.grid(row=2, column=1)

        submit_button = tk.Button(win, text="Submit", command= lambda: self.getSubmitedStory(win, name_entry, description_entry, sp_entry))
        submit_button.grid(row=3, column=0)

        submit_button = tk.Button(win, text="Cancel", command= lambda: self.cancelSubmitedStory(win, name_entry, description_entry, sp_entry))
        submit_button.grid(row=3, column=1)

    def getStoryIndex(self, story_name):
        for i in range(self.list_boxes["Stories"][1].size()):
            if(self.list_boxes["Stories"][1].get(i) == story_name):
                return i
        return 0

    # get the new story data given by the user, and 
    def getSubmitedTask(self, widget, story_name, name_entry, description_entry):
        name = name_entry.get()
        description = description_entry.get("1.0", tk.END)
        if name != "":
            list_box = self.list_boxes["Tasks"][1]
            list_size = list_box.size()
            list_box.insert(list_size, "E{}/T{}: ".format(self.getStoryIndex(story_name), list_size) + name)
            story_name = story_name[story_name.find(":")+2:]
            story_id = getById("estorias", story_name)
            story = selectAllbyID("estorias", story_id[0][0])
            print(story, story_id)
            insertTarefa(story_id[0][0], name, description, False)
            name_entry.destroy()
            widget.destroy()
        else:
            # popup an error message and keeps the window open
            Errorlabel = tk.Label(widget, text="description not given", background="red", fg="white")
            Errorlabel.grid(row=2,column=0)    

    def deleteYesButtonTask(self, widget, list_selected, task_selected):
        for i in range(list_selected.size()):
            if(list_selected.get(i) == task_selected):
                list_selected.delete(i)
                break
        task_id = getById("tarefas", task_selected[task_selected.find(":")+2:])[0][0]
        deleteByID("tarefas", task_id)
        widget.destroy()

    def deleteNoButton(self, widget):
        widget.destroy()

    # Create the delete story window popup
    def deleteTask(self):
        win = tk.Toplevel()
        win.wm_title("Window")
        task_selected = self.list_boxes["Tasks"][1].get(tk.ACTIVE)
        label= tk.Label(win, text="Are you sure you want to delete '{}' ?".format(task_selected),font=10)
        label.grid(row=0)

        yes_button = tk.Button(win, text="yes", command= lambda: self.deleteYesButtonTask(win, self.list_boxes["Tasks"][1], task_selected))
        yes_button.grid(row=4, column=1)

        no_button = tk.Button(win, text="no", command= lambda: self.deleteNoButton(win))
        no_button.grid(row=4, column=2)

    def createNewTask(self):
        win = tk.Toplevel()
        win.wm_title("Window")

        story_selected = self.list_boxes["Stories"][1].get(tk.ACTIVE)

        label= tk.Label(win, text="New task from {}".format(story_selected[story_selected.find(":")+2:]),font=10)
        label.grid(row=0)

        label= tk.Label(win, text="Task name: ",font=7)
        label.grid(row=1)
        name_entry = tk.Entry(win)
        name_entry.grid(row=1, column=1)

        label = tk.Label(win, text="Description: ",font=10)
        label.grid(row=2)
        description_entry = tk.Text(win)
        description_entry.grid(row=2, column=1)

        submit_button = tk.Button(win, text="Submit", command= lambda: self.getSubmitedTask(win, story_selected, name_entry, description_entry))
        submit_button.grid(row=3, column=0)

        cancel_button = tk.Button(win, text="Cancel", command= lambda: self.cancelSubmitedStory(win, name_entry, description_entry))
        cancel_button.grid(row=3, column=1)

        card = Canvas(win, width=74, height=97, bg='blue')
        card.place(x=300, y=600,anchor=CENTER)
        card.bind("<B1-Motion>", drag)


    def deleteYesButton(self, widget, list_selected, story_selected):
        for i in range(list_selected.size()):
            if(list_selected.get(i) == story_selected):
                list_selected.delete(i)
                break
        story_id = getById("estorias", story_selected[story_selected.find(":")+2:])[0][0]
        deleteByID("estorias", story_id)
        widget.destroy()

    def deleteNoButton(self, widget):
        widget.destroy()

    # Create the delete story window popup
    def deleteStory(self):
        win = tk.Toplevel()
        win.wm_title("Window")
        story_selected = self.list_boxes["Stories"][1].get(tk.ACTIVE)
        label= tk.Label(win, text="Are you sure you want to delete '{}' ?".format(story_selected),font=10)
        label.grid(row=0)

        yes_button = tk.Button(win, text="yes", command= lambda: self.deleteYesButton(win, self.list_boxes["Stories"][1], story_selected))
        yes_button.grid(row=4, column=1)

        no_button = tk.Button(win, text="no", command= lambda: self.deleteNoButton(win))
        no_button.grid(row=4, column=2)
        
    def changeStory(self, story_selected_name, description_widget, points_widget):
        points = points_widget.get()
        description = description_widget.get("1.0", tk.END)
        story_name = story_selected_name[story_selected_name.find(":")+2:]
        story_id = getById("estorias", story_name)
        print(story_id[0][0], story_name, description, points)
        updateEstoria(story_id[0][0], story_name, description, points)


    def storyWindow(self, story_selected_name, description, storyPoint):
        win = tk.Toplevel()
        win.wm_title("Window")

        label= tk.Label(win, text="{}".format(story_selected_name),font=10)
        label.grid(row=0, columnspan=3)
        
        description_label = tk.Label(win, text="Story points", font=6)
        description_label.grid(row=1, column=0)

        description_entry = tk.Entry(win)
        description_entry.insert(tk.END, storyPoint)
        description_entry.grid(row=1, column=1)

        description_label = tk.Label(win, text="Description", font=6)
        description_label.grid(row=2, columnspan=3)

        description_text = tk.Text(win)
        description_text.insert("1.0", description)
        description_text.grid(row=3, columnspan=3)

        yes_button = tk.Button(win, text="ok", command= lambda: self.changeStory(story_selected_name, description_text, description_entry))
        yes_button.grid(row=4, column=0)

        no_button = tk.Button(win, text="cancel", command= lambda: self.deleteNoButton(win))
        no_button.grid(row=4, column=2)        

       
def drag(event):
    event.widget.place(x=event.x_root, y=event.y_root,anchor=CENTER)

