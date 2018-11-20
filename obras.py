# encoding: 'utf-8'
from tkinter import *
from datetime import datetime
from constantes import TITULOS_OBRAS
from comandos import criar_titulos, picture

class Obra:
    def __init__(self, nome, rua, numero, bairro, cidade, telefone, contato, cei=0):
        self.id = None
        self.nome = nome
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.telefone = telefone
        self.contato = contato
        self.cei = cei
        self.orcamento = 0.00
        self.receita = []
        self.despesa = []
        self.materiais = []

    def add_orcamento(self):
        print(' - Informe o Orçamento -')
        titulo = input('Título: ').strip()
        if titulo != None:
            self.orcamento[titulo] = float(input('Informe o valor: '))
        else:
            pass

    def add_receita(self):
        print(' - Lançando Receita: - ')
        descricao = input('Descrição: ')
        valor = float(input('Informe o valor: '))
        self.receita.append([datetime.now().strftime('%d/%m/%y %H:%M:%S'), descricao, valor])

    def add_despesa(self):
        print(' - Lançando Despesa: - ')
        descricao = input('Descrição: ')
        valor = float(input('Informe o valor: '))
        self.despesa.append([datetime.now().strftime('%d/%m/%y %H:%M:%S'), descricao, valor])

    def add_materiais(self):
        print(' - Lançando Materiais: - ')
        nome = input('Nome: ')
        valor = float(input('Informe o valor: '))
        self.materiais.append([datetime.now().strftime('%d/%m/%y %H:%M:%S'), nome, valor])
        self.despesa.append([nome, valor])

    def salvar_obra(self):
        print('Salvando arquivo...')
        arquivo = open('obras.txt', 'a')
        arquivo.write('{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}\n'.format(self.nome, self.rua, self.numero, self.bairro, self.cidade, self.telefone, self.contato, self.cei, self.orcamento, self.receita, self.despesa, self.materiais))
        arquivo.close()
        print('Arquivo salvo!')

    def bd(self):
        pass

class WinObras(object):
    def __init__(self):
        self.win = Toplevel()
        self.win.geometry('500x400+250+100')
        self.win.title('Obras')
        self.win.iconbitmap('icon.ico')
        self.win.resizable(False, False)

        criar_titulos(TITULOS_OBRAS, self.win)

        self.img_cancelar = picture('images/cancelar.png', 30)
        self.img_salvar = picture('images/salvar.png', 25)
        self.img_editar = picture('images/editar.png', 30)
        self.img_novo = picture('images/novo.png', 30)
        self.img_direita = picture('images/direita.png', 30)
        self.img_esquerda = picture('images/esquerda.png', 30)
        self.img_aplicar = picture('images/aplicar.png', 40)

        # INFO
        self.info = Label(self.win)

        # ENTRY
        self.ent_nome = Entry(self.win, width=50)
        self.ent_rua = Entry(self.win, width=50)
        self.ent_numero = Entry(self.win, width=5)
        self.ent_bairro = Entry(self.win, width=20)
        self.ent_cidade = Entry(self.win, width=30)
        self.ent_tel = Entry(self.win, width=10)
        self.ent_contato = Entry(self.win, width=40)
        self.ent_cei = Entry(self.win, width=10)

