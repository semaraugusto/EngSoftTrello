from tkinter import *




class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Sistema de Auxilio em Desenvolvimento de Software")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome da Estoria", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.estoria = Label(self.terceiroContainer, text="Descricao da Estoria", font=self.fontePadrao)
        self.estoria.pack(side=LEFT)
  
        self.descricao = Entry(self.terceiroContainer)
        self.descricao["font"] = self.fontePadrao
        self.descricao.pack(side=LEFT)
  
        self.salvar = Button(self.quartoContainer)
        self.salvar["text"] = "Salvar"
        self.salvar["font"] = ("Calibri", "8")
        self.salvar["command"] = self.salvaEstoria
        self.salvar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Método verificar senha
    def salvaEstoria(self):
        tituloEstoria = self.nome.get()
        descricaoEstoria = self.descricao.get()
        

  
  
root = Tk()
Application(root)
root.mainloop()