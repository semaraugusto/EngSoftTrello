import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
import random
from banco import *
from InitialScreen import InitialPage

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        # Initializing Main label in the frame
        win = tk.Label(self, width=800, height=600)
        win.pack(pady=10,padx=10)

        label= tk.Label(win, text="Login",font=10)
        label.grid(row=0)
        name_entry = tk.Entry(win)
        name_entry.grid(row=0, column=1)


        label= tk.Label(win, text="password", font=10)
        label.grid(row=1)
        description_entry = tk.Entry(win)
        description_entry.grid(row=1, column=1)

        submit_button = tk.Button(win, text="Submit", command= lambda: self.getLoginData(win, controller, name_entry, description_entry))
        submit_button.grid(row=2, column=1)

        submit_button = tk.Button(win, text="Cancel", command= lambda: self.cancelLogin(win, name_entry, description_entry))
        submit_button.grid(row=2, column=2)

    # get the new project data given by the user, and 
    def getLoginData(self, widget, controller, name_entry, description_entry):
        Errorlabel = tk.Label(widget, text="", background="red", fg="white")
        Errorlabel.grid(row=2,column=0)
        login = name_entry.get()
        password = description_entry.get()
        if login != "" and password != "":
            print(login, password)
            if login != "adm" or password != "0000":
                Errorlabel.destroy()
                Errorlabel = tk.Label(widget, text="Invalid login or password", background="red", fg="white")
                Errorlabel.grid(row=2,column=0)

            elif login == "adm" and password == "0000":
                controller.show_initialframe(0)
                name_entry.destroy()
                widget.destroy()
        else:
            # popup an error message and keeps the window open
            Errorlabel.destroy()
            Errorlabel = tk.Label(widget, text="login or password not given", background="red", fg="white")
            Errorlabel.grid(row=2,column=0)

    def cancelLogin(self, widget, name_entry, description_entry):
        name_entry.destroy()
        description_entry.destroy()
        widget.destroy()