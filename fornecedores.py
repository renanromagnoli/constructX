# encoding: 'utf-8'
from tkinter import *
from comandos import criar_titulos, picture
from constantes import TITULOS_FORNECEDORES


class Fornecedor:
    def __init__(self, nome, rua, numero, bairro, cidade, descricao):
        self.nome = nome
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.descricao = descricao

    def salvar_fornecedor(self):
        arquivo = open('fornecedores.txt', 'a')
        arquivo.write('{}_{}_{}_{}_{}_{}'.format(self.nome, self.rua, self.numero, self.bairro, self.cidade, self.descricao))
        arquivo.close()


class WinFornecedores:
    def __init__(self):

        # ESTRUTURA TKINTER
        self.win = Tk()
        self.win.geometry('450x350+400+150')
        self.win.resizable(False, False)
        self.win.iconbitmap('icon.ico')
        self.win.title('Fornecedores')

        # IMAGENS
        #self.img_aplicar = picture('images/aplicar.png', 40)

        # LABELS
        criar_titulos(TITULOS_FORNECEDORES, self.win)
        self.info = Label(self.win, text='')

        # ENTRADAS
        self.nome = Entry(self.win, width=50)
        self.rua = Entry(self.win, width=50)
        self.numero = Entry(self.win, width=4)
        self.bairro = Entry(self.win)
        self.cidade = Entry(self.win)
        self.tel = Entry(self.win)
        self.descricao = Text(self.win, width=40, height=5)

        # BOTÕES
        self.btn_aplicar = Button(self.win, text='Aplicar')
        self.btn_editar = Button(self.win, text='Editar')
        self.btn_cancelar = Button(self.win, text='Editar')
        self.btn_direita = Button(self.win, text='>')
        self.btn_esquerda = Button(self.win, text='<')

        # EMPACOTAMENTOS
        self.info.grid(row=0, column=2, sticky=W)
        self.nome.grid(row=1, column=2, sticky=W)
        self.rua.grid(row=2, column=2, sticky=W)
        self.numero.grid(row=3, column=2, sticky=W)
        self.bairro.grid(row=4, column=2, sticky=W)
        self.cidade.grid(row=5, column=2, sticky=W)
        self.tel.grid(row=6, column=2, sticky=W)
        self.descricao.grid(row=7, column=2, sticky=W)

        self.btn_aplicar.grid(row=8, column=2, sticky=E, padx=10, pady=10)

        self.win.mainloop()



