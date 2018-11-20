# encoding: 'utf-8'

from tkinter import *
from constantes import EMPRESA_NOME, TITULOS_DESPESAS
from comandos import criar_titulos
from datetime import date

class WinDespesas(object):

    def __init__(self):

        self.win = Toplevel()
        self.win.geometry('350x280+500+200')
        self.win.iconbitmap('icon.ico')
        self.win.title('{} - Despesas'.format(EMPRESA_NOME))
        self.win.resizable(None, None)

        # TÍTULOS
        criar_titulos(TITULOS_DESPESAS, self.win)

        # INFO
        self.info = Label(self.win)

        # COMBOBOX
        self.ob = StringVar()
        self.com_obra = ttk.Combobox(self.win, textvariable=self.ob)
        self.com_obra['values'] = ('Obra 1', 'Obra 2')

        # ENTRADAS
        self.ent_valor = Entry(self.win, width=15)
        self.ent_data = Entry(self.win, width=8)
        self.ent_venc = Entry(self.win, width=8)
        self.txt_descricao = Text(self.win, width=30, height=5)

        # BOTÕES
        self.btn_lancar = Button(self.win, text='Lançar Despesa')

        # EMPACOTAMENTOS
        self.info.grid(row=1, column=2, sticky=W)
        self.com_obra.grid(row=2, column=2, sticky=W)
        self.ent_valor.grid(row=3, column=2, sticky=W)
        self.ent_data.grid(row=4, column=2, sticky=W)
        self.ent_venc.grid(row=5, column=2, sticky=W)
        self.txt_descricao.grid(row=6, column=2, sticky=W)
        self.btn_lancar.grid(row=7, column=2, sticky=E, pady=10)

        # INSERT PADRÃO
        self.ent_valor.insert(END, '0,00')
        self.ent_data.insert(END, date.today().strftime('%d/%m/%y'))
        self.ent_venc.insert(END, date.fromordinal(date.today().toordinal() + 30).strftime('%d/%m/%y'))

        self.win.mainloop()

    def lancar(self):
        pass