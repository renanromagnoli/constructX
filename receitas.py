# encoding: 'utf-8'

from tkinter import *
from tkinter import ttk
from constantes import EMPRESA_NOME, TITULOS_RECEITAS
from comandos import criar_titulos, picture
from datetime import date

class WinReceitas(object):

    def __init__(self):
        self.win = Toplevel()
        self.win.geometry('350x280+500+200')
        self.win.iconbitmap('icon.ico')
        self.win.title('{} - Receitas'.format(EMPRESA_NOME))

        # TÍTULOS
        criar_titulos(TITULOS_RECEITAS, self.win)


        # IMAGENS
        self.img_direita = picture('images/direita.png', 30)
        self.img_esquerda = picture('images/esquerda.png', 30)

        self.info = Label(self.win, text='')
        # ENTRADAS
        self.ent_cliente = Entry(self.win, width=30)
        self.ent_valor = Entry(self.win, width=15)
        self.ent_data = Entry(self.win, width=8)
        self.txt_descricao = Text(self.win, width=30, height=5)

        # COMBOBOX
        self.ob = StringVar()
        self.com_obra = ttk.Combobox(self.win, textvariable=self.ob)
        self.com_obra['values'] = ('Obra 1', 'Obra 2')


        # BOTÕES
        self.btn_receber = Button(self.win, text='Receber', command = self.receber)

        # EMPACOTAMENTOS
        self.info.grid(row=1, column=2, sticky=W)
        self.ent_cliente.grid(row=2, column=2, sticky=W)
        self.com_obra.grid(row=3, column=2, sticky=W)
        self.ent_valor.grid(row=4, column=2, sticky=W)
        self.ent_data.grid(row=5, column=2, sticky=W)
        self.txt_descricao.grid(row=6, column=2, sticky=W)
        self.btn_receber.grid(row=7, column=2, sticky=E, pady=10)

        # INSERT PADRÃO
        self.ent_data.insert(END, date.today().strftime('%d/%m/%y'))
        self.ent_valor.insert(END, '0,00')



        self.win.mainloop()

    def receber(self):
        self.info['text'] = 'Receita lançada!'
        self.info['fg'] = 'green'