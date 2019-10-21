import tkinter as tk
from tkinter import messagebox
from tkinter import font  as tkfont
import random
from banco import *
import security
import InitialScreen


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

        inicializaBanco()

        label= tk.Label(win, text="password", font=10)
        label.grid(row=1)
        description_entry = tk.Entry(win)
        description_entry.grid(row=1, column=1)

        submit_button = tk.Button(win, text="Submit", command= lambda: self.getLoginData(win, controller, name_entry, description_entry))
        submit_button.grid(row=3, column=2)

        submit_button = tk.Button(win, text="Cancel", command= lambda: self.cancelLogin(win, name_entry, description_entry))
        submit_button.grid(row=3, column=3)

        submit_button = tk.Button(win, text="Create new User", command= lambda: self.createNewUser())
        submit_button.grid(row=3, column=1)

    # get the new project data given by the user, and 
    def getLoginData(self, widget, controller, name_entry, pass_entry):
        Errorlabel = tk.Label(widget, text="", background="red", fg="white")
        Errorlabel.grid(row=2,column=0)
        login = name_entry.get()
        password = pass_entry.get()
        if login != "" and password != "":
            #print(login, password, security.criptografaSenha(password))
            if not confirmaLogin(login, password):
                Errorlabel.destroy()
                Errorlabel = tk.Label(widget, text="Invalid login or password", background="red", fg="white")
                Errorlabel.grid(row=2,column=0)
                name_entry.delete(0, 'end')
                pass_entry.delete(0, 'end')

            else:
                command = "SELECT id FROM usuarios WHERE nome = '{a}';"
                command = command.format(a=login)
                cur_user_id = executeQuery(command)[0][0]

                controller.show_initialframe(cur_user_id)
                name_entry.destroy()
                widget.destroy()
        else:
            # popup an error message and keeps the window open
            Errorlabel.destroy()
            Errorlabel = tk.Label(widget, text="login or password not given", background="red", fg="white")
            Errorlabel.grid(row=2,column=0)

    def cancelLogin(self, widget, name_entry, pass_entry):
        name_entry.destroy()
        pass_entry.destroy()
        widget.destroy()

    # Create the new user window popup to get the new user data
    def createNewUser(self):
        win = tk.Toplevel()
        win.wm_title("New User Window")

        label= tk.Label(win, text="User Name",font=10)
        label.grid(row=1)
        label= tk.Label(win, text="Password",font=10)
        label.grid(row=2)
        label= tk.Label(win, text="Equipe",font=10)
        label.grid(row=3)
        name_entry = tk.Entry(win)
        name_entry.grid(row=1, column=1)
        pass_entry = tk.Entry(win)
        pass_entry.grid(row=2, column=1)
        equipe_entry = tk.Entry(win)
        equipe_entry.grid(row=3, column=1)

        submit_button = tk.Button(win, text="Submit", command= lambda: self.getSubmitedUser(win, name_entry, pass_entry, equipe_entry))
        submit_button.grid(row=4, column=1)

        submit_button = tk.Button(win, text="Cancel", command= lambda: self.cancelSubmitedUser(win, name_entry, pass_entry, equipe_entry))
        submit_button.grid(row=4, column=0)

    # get the new project data given by the user, and 
    def getSubmitedUser(self, widget, name_entry, pass_entry, equipe_entry):
        name = name_entry.get()
        pwd = pass_entry.get()
        equipe = equipe_entry.get()

        if name != "" and pwd != "" and equipe != "":

            id_equipe = checaEquipes(equipe)
            try:
                insertUsuario(name, pwd, id_equipe)
            except:
                # popup an error message and keeps the window open
                Errorlabel = tk.Label(widget, text="user already exists", background="red", fg="white")
                Errorlabel.grid(row=2,column=0)
                return

            label = tk.Label(widget, text="User created successfully")
            label.grid(row=2,column=0)

            name_entry.destroy()
            pass_entry.destroy()
            widget.destroy()

        else:
            # popup an error message and keeps the window open
            Errorlabel = tk.Label(widget, text="Name or password or equipe not given", background="red", fg="white")
            Errorlabel.grid(row=2,column=0)

    def cancelSubmitedUser(self, widget, name_entry, pass_entry, equipe_entry):
        name_entry.destroy()
        pass_entry.destroy()
        equipe_entry.destroy()
        widget.destroy()
