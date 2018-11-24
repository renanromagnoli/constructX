#coding: 'utf-8'
import sqlite3
from datetime import date
from tkinter import *
from tkinter import ttk
from constantes import TITULOS_CADASTRO_FUNCIONARIO
from comandos import criar_titulos, picture

# Classe para criar o objeto de Funcionário
class Funcionario(object):
    def __init__(self, nome, nascimento, tel, rg, ctps, endereco, cidade, obra=0, admissao=date.today()):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__tel = tel
        self.__rg = rg
        self.__ctps = ctps
        self.__endereco = endereco
        self.__cidade = cidade
        self.__vale = []
        self.__admissao = admissao
        self.__ferias = []
        self.__previsao_ferias = None
        self.__retorno_ferias = None
        self.__faltas = 0
        self.__obra_id = obra

    def get_nome(self):
        return self.__nome

    def set_nome(self, x):
        self.__nome = x

    def get_nascimento(self):
        return self.__nascimento

    def set_nascimento(self, x):
        self.__nascimento = x

    def get_tel(self):
        return self.__tel

    def set_tel(self, x):
        self.__tel = x

    def get_rg(self):
        return self.__rg

    def set_rg(self, x):
        self.__rg = x

    def get_ctps(self):
        return self.__ctps

    def set_ctps(self, x):
        self.__ctps = x

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, x):
        self.__endereco = x

    def get_cidade(self):
        return self.__cidade

    def set_cidade(self, x):
        self.__cidade = x

    def get_vale(self):
        return self.__vale

    def set_vale(self, x):
        self.__vale.append(x)

    def get_admissao(self):
        return self.__admissao

    def set_adminissao(self, x):
        self.__admissao = x

    def get_ferias(self):
        return self.__ferias

    def set_ferias(self, x):
        self.__ferias.append(x)

    def get_prev_ferias(self):
        return self.__previsao_ferias

    def set_prev_ferias(self, x):
        self.__previsao_ferias = x

    def get_ret_ferias(self):
        return self.__retorno_ferias

    def set_ret_ferias(self, x):
        self.__retorno_ferias = x

    def get_faltas(self):
        return self.__faltas

    def set_faltas(self):
        self.__faltas += 1

    def get_obra_id(self):
        return self.__obra_id

    def set_obra_id(self, x):
        self.__obra_id = x

    # Método "Prever Férias"
    def prev_ferias(self, tempo=720):
        if self.get_ret_ferias() == None:
            self.set_prev_ferias(date.fromordinal(self.get_admissao().toordinal() + tempo))
        else:
            self.set_prev_ferias(date.fromordinal(self.get_ret_ferias().toordinal() + tempo))
        return self.get_prev_ferias()


    def tirarferias(self, dias):
        self.__ferias.append('{} - {}'.format(date.today(), dias))


    def cadastrar_funcionario(self):
        pass

# Classe  para criação do objeto janela Funcionários
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
        self.btn_novocadastro = Button(self.win, image=self.img_novo, command=self.__novo_cadastro, borderwidth=0)
        self.btn_aplicar_editar = Button(self.win, borderwidth=0, )
        self.btn_cancelar = Button(self.win, image=self.img_cancelar, borderwidth=0, text='Cancelar', command=self.cancelar)
        self.btn_direita = Button(self.win, image=self.img_direita, command=self.direita, borderwidth=0)
        self.btn_esquerda = Button(self.win, image=self.img_esquerda, command=self.esquerda, borderwidth=0)

        '''self.btn_novocadastro.image = img_novo
        self.btn_cancelar.image = img_cancelar
        self.btn_direita.image = img_direita
        self.btn_esquerda.image = img_esquerda'''


        # EMPACOTAMENTOS
        self.info.grid(row=0, column=2, sticky=W)
        self.nome.grid(row=1, column=2, sticky=W)
        self.nascimento.grid(row=2, column=2, sticky=W)
        self.tel.grid(row=3, column=2, sticky=W)
        self.rg.grid(row=4, column=2, sticky=W)
        self.endereco.grid(row=5, column=2, sticky=W)
        self.cidade.grid(row=6, column=2, sticky=W)
        self.obras.grid(row=7, column=2, sticky=W)
        self.data_admissao.grid(row=8, column=2, sticky=W)
        self.contrato_exp.grid(row=9, column=2, sticky=W)

        self.btn_saveclose.grid(row=10, column=2, sticky=E, ipadx=10)
        self.btn_novocadastro.grid(row=12, column=2, ipadx=10)
        self.btn_aplicar_editar.grid(row=12, column=2, stick=E, ipadx=10)

        # VERIFICANDO SE NO BANCO DE DADOS JÁ EXISTEM REGISTRO DE FUNCIONÁRIOS
        data = sqlite3.connect('bd.sqlite')
        cur = data.cursor()
        if cur.execute('SELECT nome FROM Funcionarios').fetchone() == None:
            self.set_acesso('normal')
        else:
            self.set_acesso('disable')
        cur.close()

        self.win.mainloop()



    # FUNÇÃO PARA O CHECK BUTTON
    def contrato_exp(self):
        self.var_exp = not self.var_exp
        print(self.var_exp)
        return self.var_exp

    # STATE = NORMAL/DISABLE
    def __acesso(self, estado):
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

            self.btn_saveclose.grid(row=12, column=2, sticky=W)
            self.btn_cancelar.grid(row=12, column=1, sticky=W, pady=5, padx=30)
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

            self.btn_direita.grid(row=12, column=1, sticky=E, padx=40, pady=10)
            self.btn_esquerda.grid(row=12, column=1, sticky=W, padx=40, pady=10)

    def set_acesso(self, x):
        self.__acesso(x)

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
            print(self.cur.execute('SELECT nome FROM Funcionarios WHERE nome = ?', (self.func.get_nome(), )).fetchone())

            if self.cur.execute('SELECT nome FROM Funcionarios WHERE nome = ?', (self.func.get_nome(), )).fetchone() == None:
                self.cur.execute('''INSERT INTO Funcionarios (nome, nascimento, tel, rg, ctps, endereco, cidade, obra_id, admissao) 
                                            VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (self.func.get_nome(), self.func.get_nascimento(), self.func.get_tel(), self.func.get_rg(), self.func.get_ctps(),
                             self.func.get_endereco(), self.func.get_cidade(), self.func.get_obra_id(), self.func.get_admissao()))
                self.data.commit()
                self.cur.close()
                self.info['text'] = 'Cadastrado realizado com sucesso!'
                self.info['fg'] = 'green'
            else:
                self.atualizando(self.func.get_nome(), self.func.get_nascimento(), self.func.get_tel(), self.func.get_rg(), self.func.get_ctps(), self.func.get_endereco(), self.func.get_cidade(), self.func.get_obra_id(), self.func.get_admissao(), self.func.get_nome())

            self.__acesso('disable')

    # FUNÇÃO PARA O BOTÃO EDITAR
    def editando(self):
        print('Editando')
        self.set_acesso('normal')

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

    def __novo_cadastro(self):
        self.__acesso('normal')
        self.nome.delete(0, END)
        self.nascimento.delete(0, END)
        self.tel.delete(0, END)
        self.rg.delete(0, END)
        self.endereco.delete(0, END)

    def salvar_novo(self):
        self.salvar()
        self.__novo_cadastro()

    def deseja_atualizar(self):
        pass

    # FUNÇÃO PARA O BOTÃO SALVAR E FECHAR
    def salvar_e_fechar(self):

        self.salvar()
        self.win.destroy()

        print('Cadastrado')
        print('{}\n{}\n{}\n{}\n{}'.format(self.func.get_nome(), self.func.get_nascimento(), self.func.get_rg(), self.func.get_endereco(), self.func.get_cidade()))

        self.win.destroy()

    # FUNÇÃO CANCELAR
    def cancelar(self):
        print('cancelado')
        self.set_acesso('disable')

