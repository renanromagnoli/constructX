#coding: 'utf-8'
import sqlite3
from datetime import date
from tkinter import *
from tkinter import ttk
from constantes import TITULOS_CADASTRO_FUNCIONARIO
from comandos import criar_titulos, picture

class Funcionario(object):
    def __init__(self, nome, nascimento, tel, rg, ctps, endereco, cidade, obra=0, admissao=date.today()):
        self.nome = nome
        self.nascimento = nascimento
        self.tel = tel
        self.rg = rg
        self.ctps = ctps
        self.endereco = endereco
        self.cidade = cidade
        self.vale = []
        self.admissao = admissao
        self.ferias = []
        self.previsaoferias = None
        self.retornoferias = None
        self.faltas = 0
        self.obra_id = obra

    def prevferias(self, tempo=720):
        if self.retornoferias == None:
            self.previsaoferias = date.fromordinal(self.admissao.toordinal() + tempo)
        else:
            self.previsaoferias = date.fromordinal(self.retornoferias.toordinal() + tempo)
        return self.previsaoferias

    def addfalta(self, quantidade):
        self.faltas += quantidade

    def tirarferias(self, dias):
        self.ferias.append('{} - {}'.format(date.today(), dias))


    def cadastrar_funcionario(self):
        pass

# Classe Tkinter para janela Funcionários
class WinFuncionarios(object):
    def __init__(self):

        self.win = Toplevel()
        self.win.geometry('500x350+400+150')
        self.win.title('Funcionários')
        self.win.iconbitmap('icon.ico')
        self.win.resizable(False, False)

        criar_titulos(TITULOS_CADASTRO_FUNCIONARIO, self.win)

        # IMAGENS
        #self.img_cancelar = PhotoImage(file='images/cancelar.png')
        self.img_cancelar = picture('images/cancelar.png', 30)
        self.img_salvar = picture('images/salvar.png', 25)
        self.img_editar = picture('images/editar.png', 30)
        self.img_novo = picture('images/novo.png', 30)
        self.img_direita = picture('images/direita.png', 30)
        self.img_esquerda = picture('images/esquerda.png', 30)
        self.img_aplicar = picture('images/aplicar.png', 40)



        # INFO
        self.info = Label(self.win, text='')

        # CAMPOS ENTRY
        self.nome = Entry(self.win, width='50')
        self.nascimento = Entry(self.win)
        self.tel = Entry(self.win)
        self.rg = Entry(self.win)
        self.endereco = Entry(self.win, width='50')
        self.cidade = Entry(self.win)
        # self.obra = Menu(janela)
        self.data_admissao = Entry(self.win, width='8')

        # COMBOBOXES (Obras)
        self.ob = StringVar()
        self.obras = ttk.Combobox(self.win, textvariable=self.ob)
        self.obras['values'] = ('Ex1', 'Ex2', 'Ex3')

        # 'INSERT (END' - Text Widget para inserir campo
        self.cidade.insert(END, 'Ponte Nova')
        self.data_admissao.insert(END, date.today().strftime('%d/%m/%y'))

        # CHECK BUTTON
        self.var_exp = IntVar()
        self.var_exp = not self.var_exp
        self.contrato_exp = Checkbutton(self.win, variable=self.var_exp, command=self.contrato_exp)

        # BOTÕES
        self.btn_saveclose = Button(self.win, text='Salvar e Fechar', command=self.salvar_e_fechar, borderwidth=0)
        self.btn_novocadastro = Button(self.win, image=self.img_novo, command=self.novo_cadastro, borderwidth=0)
        self.btn_aplicar_editar = Button(self.win, borderwidth=0, )
        self.btn_cancelar = Button(self.win, image=self.img_cancelar, borderwidth=0, text='Cancelar', command=self.cancelar)
        self.btn_direita = Button(self.win, image=self.img_direita, command=self.direita, borderwidth=0)
        self.btn_esquerda = Button(self.win, image=self.img_esquerda, command=self.esquerda, borderwidth=0)

        '''self.btn_novocadastro.image = img_novo
        self.btn_cancelar.image = img_cancelar
        self.btn_direita.image = img_direita
        self.btn_esquerda.image = img_esquerda'''


        # EMPACOTAMENTOS
        self.info.grid(row=1, column=2, sticky=W)
        self.nome.grid(row=2, column=2, sticky=W)
        self.nascimento.grid(row=3, column=2, sticky=W)
        self.tel.grid(row=4, column=2, sticky=W)
        self.rg.grid(row=5, column=2, sticky=W)
        self.endereco.grid(row=6, column=2, sticky=W)
        self.cidade.grid(row=7, column=2, sticky=W)
        self.obras.grid(row=8, column=2, sticky=W)
        self.data_admissao.grid(row=9, column=2, sticky=W)
        self.contrato_exp.grid(row=10, column=2, sticky=W)

        self.btn_saveclose.grid(row=11, column=2, sticky=E, ipadx=10)
        self.btn_novocadastro.grid(row=13, column=2, ipadx=10)
        self.btn_aplicar_editar.grid(row=13, column=2, stick=E, ipadx=10)

        # VERIFICANDO SE NO BANCO DE DADOS JÁ EXISTEM REGISTRO DE FUNCIONÁRIOS
        data = sqlite3.connect('bd.sqlite')
        cur = data.cursor()
        if cur.execute('SELECT nome FROM Funcionarios').fetchone() == None:
            self.acesso('normal')
        else:
            self.acesso('disable')
        cur.close()

        self.win.mainloop()



    # FUNÇÃO PARA O CHECK BUTTON
    def contrato_exp(self):
        self.var_exp = not self.var_exp
        print(self.var_exp)
        return self.var_exp

    # STATE = NORMAL/DISABLE
    def acesso(self, estado):
        self.nome['state'] = estado
        self.cidade['state'] = estado
        self.endereco['state'] = estado
        self.nascimento['state'] = estado
        self.obras['state'] = estado
        self.data_admissao['state'] = estado
        self.tel['state'] = estado
        self.rg['state'] = estado

        if estado == 'normal':
            self.btn_direita.grid_forget()
            self.btn_esquerda.grid_forget()

            self.btn_saveclose.grid(row=13, column=2, sticky=W)
            self.btn_cancelar.grid(row=13, column=1, sticky=W, pady=5, padx=30)
            self.btn_saveclose['image'] = self.img_salvar
            self.btn_saveclose.image = self.img_salvar

            self.btn_aplicar_editar['command'] = self.salvar
            self.btn_aplicar_editar['text'] = 'Salvar'
            self.btn_aplicar_editar['image'] = self.img_aplicar
            self.btn_aplicar_editar.image = self.img_aplicar

            self.btn_novocadastro['text'] = 'Salvar e Novo'
            self.btn_novocadastro['command'] = self.salvar_novo

            self.contrato_exp['state'] = NORMAL



        elif estado == 'disable':

            self.btn_saveclose.grid_forget()
            self.btn_cancelar.grid_forget()

            self.btn_aplicar_editar['command'] = self.editando
            self.btn_aplicar_editar['text'] = 'Editar'
            self.btn_aplicar_editar['image'] = self.img_editar
            self.btn_aplicar_editar.image = self.img_editar

            self.btn_novocadastro['text'] = 'Novo Cadastro'
            self.btn_novocadastro['command'] = self.novo_cadastro

            self.contrato_exp['state'] = DISABLED

            self.info['text'] = ''

            # BOTÕES DIREITA E ESQUERDA

            self.btn_direita.grid(row=13, column=1, sticky=E, padx=40, pady=10)
            self.btn_esquerda.grid(row=13, column=1, sticky=W, padx=40, pady=10)


    # FUNÇÃO PARA O BOTÃO DA DIREITA
    def direita(self):
        print('Direita')
        pass

    # FUNÇÃO PARA O BOTÃO DA ESQUERDA
    def esquerda(self):
        print('Esquerda')
        pass

    # FUNÇÃO PARA O BOTÃO SALVAR
    def salvar(self):
        if self.nome.get().strip() == '':
            self.info['text'] = 'Preencha o Nome no cadastro!'
            self.info['fg'] = 'red'
        else:
            self.func = Funcionario(self.nome.get(), self.nascimento.get(), self.tel.get(), self.rg.get(), 0,
                               self.endereco.get(), self.cidade.get())
            self.data = sqlite3.connect('bd.sqlite')
            self.cur = self.data.cursor()
            print(self.cur.execute('SELECT nome FROM Funcionarios WHERE nome = ?', (self.func.nome, )).fetchone())

            if self.cur.execute('SELECT nome FROM Funcionarios WHERE nome = ?', (self.func.nome, )).fetchone() == None:
                self.cur.execute('''INSERT INTO Funcionarios (nome, nascimento, tel, rg, ctps, endereco, cidade, obra_id, admissao) 
                                            VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (self.func.nome, self.func.nascimento, self.func.tel, self.func.rg, self.func.ctps,
                             self.func.endereco, self.func.cidade, self.func.obra_id, self.func.admissao))
                self.data.commit()
                self.cur.close()
                self.info['text'] = 'Cadastrado realizado com sucesso!'
                self.info['fg'] = 'green'
            else:
                self.atualizando(self.func.nome, self.func.nascimento, self.func.tel, self.func.rg, self.func.ctps, self.func.endereco, self.func.cidade, self.func.obra_id, self.func.admissao, self.func.nome)

            self.acesso('disable')

    # FUNÇÃO PARA O BOTÃO EDITAR
    def editando(self):
        print('Editando')
        self.acesso('normal')

    # FUNÇÃO PARA ATUALIZAR O BANCO DE DADOS
    def atualizando(self, nome, nascimento, tel, rg, ctps, endereco, cidade, obra_id, admissao, referencia):
        self.cur.executescript(f'''
            UPDATE Funcionarios
            SET nome = {nome}, 
                nascimento = {nascimento}, 
                tel = {tel}, 
                rg = {rg}, 
                ctps = {ctps}, 
                endereco = {endereco}, 
                cidade = {cidade}, 
                obra_id = {obra_id}, 
                admissao = {admissao}
            WHERE nome = {referencia}
        ''')
        self.data.commit()
        self.cur.close()
        self.info['text'] = 'Cadastro Atualizado!'
        print('Cadastro atualizado')

    def novo_cadastro(self):
        self.acesso('normal')
        self.nome.delete(0, END)
        self.nascimento.delete(0, END)
        self.tel.delete(0, END)
        self.rg.delete(0, END)
        self.endereco.delete(0, END)

    def salvar_novo(self):
        self.salvar()
        self.novo_cadastro()

    def deseja_atualizar(self):
        pass

    # FUNÇÃO PARA O BOTÃO SALVAR E FECHAR
    def salvar_e_fechar(self):

        self.salvar()
        self.win.destroy()

        print('Cadastrado')
        print('{}\n{}\n{}\n{}\n{}'.format(func.nome, func.nascimento, func.rg, func.endereco, func.cidade))

        self.win.destroy()

    # FUNÇÃO CANCELAR
    def cancelar(self):
        print('cancelado')
        self.acesso('disable')

