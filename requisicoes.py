# encoding: 'utf-8'

from tkinter import *
from tkinter import ttk
from constantes import EMPRESA_NOME, TITULOS_REQUISICOES
from comandos import criar_titulos

class WinRequisicoes(object):

    def __init__(self):
        self.win = Tk()
        self.win.geometry('360x360+500+200')
        self.win.iconbitmap('icon.ico')
        self.win.title('{} - Requisições'.format(EMPRESA_NOME))
        self.win.resizable(None, None)

        # TÍTULOS
        criar_titulos(TITULOS_REQUISICOES, self.win)

        # INFO
        self.info = Label(self.win)

        # COMBOBOX
        ob = StringVar()
        self.com_obra = ttk.Combobox(self.win, textvariable=ob)
        self.com_obra['values'] = ('Obra 1', 'Obra 2')

        forn = StringVar()
        self.com_fornecedor = ttk.Combobox(self.win, textvariable=forn)
        self.com_fornecedor['values'] = ('Construbel', 'Construnova', 'Eletrilar')

        # LABELS
        self.lab_usuario = Label(self.win, text='Renan')

        # ENTRADAS
        self.txt_material = Text(self.win, width=30, height=5)
        self.ent_valor = Entry(self.win, width=10)
        self.txt_observacao = Text(self.win, width=30, height=5)

        # BOTÕES
        self.btn_enviar = Button(self.win, text='Enviar Requisicação')

        # EMPACOTAMENTOS
        self.info.grid(row=1, column=2, sticky=W)
        self.lab_usuario.grid(row=2, column=2, sticky=W)
        self.com_obra.grid(row=3, column=2, sticky=W)
        self.com_fornecedor.grid(row=4, column=2, sticky=W)
        self.txt_material.grid(row=5, column=2, sticky=W)
        self.ent_valor.grid(row=6, column=2, sticky=W)
        self.txt_observacao.grid(row=7, column=2, sticky=W)
        self.btn_enviar.grid(row=8, column=2, sticky=E, pady=10)


        self.win.mainloop()

