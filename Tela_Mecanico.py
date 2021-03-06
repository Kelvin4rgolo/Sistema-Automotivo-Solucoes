from tkinter import *
from tkinter import messagebox


class Mecanico():
    def __init__(self, nome, cpf):
        self.mecNome = nome
        self.mecCPF = cpf

        self.janela = Tk()
        self.janela.title('Mecânico')
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 14)
        self.janela.maxsize(1200, 600)
        self.janela.minsize(1200, 600)
        self.janela.configure(bg='#363636')
        self.janela.minsize(width=1200, height=600)
        # self.janela.iconbitmap('automotivo.ico')

        self.LoginCanvas = Canvas(master=self.janela, width=600, height=370)
        self.LoginCanvas.pack(expand=1, fill=BOTH)

        self.Back = PhotoImage(master=self.janela, file="mecanico.png")
        self.LoginCanvas.create_image(0, 0, image=self.Back, anchor=NW)

        self.hoverColor1 = '#00BFFF'
        self.hoverColor2 = '#FF0000'

        self.botaoCadastrar = Button(self.janela, text="Cadastrar\nOrçamento", font=self.textStyles, width=15,
                                     height=3, pady=5, bg="#4682B4", fg="white", relief=RAISED, command=self.cadastrarOrcamento)
        self.LoginCanvas.create_window(900, 130, window=self.botaoCadastrar)
        self.botaoCadastrar.bind("<Enter>", self.hoverIn1)
        self.botaoCadastrar.bind("<Leave>", self.hoverOut)

        self.botaoOrdem = Button(self.janela, text="Ordem\n de \nServiço", font=self.textStyles,
                                 width=15, height=3, pady=1, bg="#4682B4", fg="white", relief=RAISED, command=self.verOrdem)
        self.LoginCanvas.create_window(900, 265, window=self.botaoOrdem)
        self.botaoOrdem.bind("<Enter>", self.hoverIn1)
        self.botaoOrdem.bind("<Leave>", self.hoverOut)

        self.botaoSair = Button(self.janela, text="SAIR", font=self.textStyles, width=5,
                                bg="#4682B4", fg="white", pady=5, relief=RAISED, command=self.saiu)
        self.LoginCanvas.create_window(900, 400, window=self.botaoSair)
        self.botaoSair.bind("<Enter>", self.hoverIn2)
        self.botaoSair.bind("<Leave>", self.hoverOut)

        self.titulo = Label(self.janela, bg='#363636',
                            fg='white', font=self.titleStyles, text='MECÂNICO')
        self.titulo.pack(padx=0, pady=10)

        mainloop()

    def cadastrarOrcamento(self):
        from cadastrarOrcamento import cadastrar_orcamento as ORCCAD
        cadastrarOrcamento = ORCCAD(self.mecNome, self.mecCPF)
        

    def hoverIn1(self, event):
        event.widget.configure(bg=self.hoverColor1, fg="white", relief=GROOVE)

    def hoverIn2(self, event):
        event.widget.configure(bg=self.hoverColor2, fg="white", relief=GROOVE)

    def hoverOut(self, event):
        event.widget.configure(bg='#4682B4', relief=RAISED)

    def saiu(self):
        self.janela.destroy()
        from Tela_Login import Tela_de_Login
        return

    def verOrdem(self):
        from visualizarOrdemMecanico import verOrdensMecanico
        return

