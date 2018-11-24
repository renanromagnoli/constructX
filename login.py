#coding: 'utf-8'

import sqlite3
from tkinter import *
from comandos import criar_titulos
from constantes import TITULOS_LOGIN
from home import WinHome


class WinLogin(object):

    def __init__(self):
        # JANELA TKINTER
        self.__win = Tk()
        self.__win.geometry('270x150+500+300')
        self.__win.iconbitmap('icon.ico')
        self.__win.title('ConstructX')
        self.__win.resizable(False, False)

        criar_titulos(TITULOS_LOGIN, self.__win)

        # INFO
        self.__info = Label(self.__win, text='')

        # ENTRADAS
        self.__user = Entry(self.__win, width='20')
        self.__senha = Entry(self.__win, width='20', show='*')

        # LEMBRAR USUÁRIO
        self.__lem = IntVar()
        #self.__lem = not self.__lem
        self.__chk_lembrar = Checkbutton(self.__win, variable=self.__lem, command=self.__lembrar)
        self.__chk_lembrar.select()

        #BOTÕES
        self.__botao = Button(self.__win, text='Entrar', command=self.login)

        # Empacotando
        self.__info.grid(row=0, column=2)
        self.__user.grid(row=1, column=2)
        self.__senha.grid(row=2, column=2)
        self.__chk_lembrar.grid(row=3, column=2, sticky=W)
        self.__botao.grid(row=4, column=2)

        # Enter no campo de Senha funcionando como o botão Entrar
        self.__user.bind("<KeyPress>", lambda u: self.login() if u.char == '\r' else None)

        # Enter no campo de Senha funcionando como o botão Entrar
        self.__senha.bind("<KeyPress>", lambda s: self.login() if s.char == '\r' else None)


        self.__cache()

        self.__win.mainloop()

    def login(self):
        if self.__check_login() == True:
            if self.__lem and self.__cache() == False:
                self.__lembrando()
            self.__win.destroy()
            WinHome()

    def logoff(self):
        self.__win.destroy()
        WinLogin()

    def __lembrar(self):
        self.__lem = not self.__lem
        print(self.__lem)

    def __check_login(self):
        __nome = self.__get_login()[0]
        __senha = self.__get_login()[1]
        __dados = sqlite3.connect('bd.sqlite')
        __cur = __dados.cursor()
        __cur.execute('SELECT nome, senha FROM Users')
        __registros = __cur.fetchall()
        for x in __registros:
            print(x)
            if x[0] == __nome and __senha == x[1]:
                self.player = x[0]
                print('{} está logado!'.format(__nome))
                self.__info['text'] ='Login realizado!'
                self.__info['fg'] = 'green'
                __cur.close()

                return True
            else:
                continue
        print('Usuário e Senha inválidos!')
        self.__info['text'] = 'Acesso inválido!'
        self.__info['fg'] = 'red'
        __cur.close()
        return False

    def get_user(self):
        dados = sqlite3.connect('bd.sqlite')
        cur = dados.cursor()
        cur.execute('SELECT id, grupo_id, nome FROM Users WHERE nome = ?', (self.player, ))
        select = cur.fetchone()
        dados.close()
        return select

    def __get_login(self):
        return self.__user.get(), self.__senha.get()

    def __set_login(self, usuario, senha):
        self.__user.insert(END, usuario)
        self.__senha.insert(END, senha)

    def __lembrando(self):
        with open('login.txt', 'w') as login:
           login.write('{}:{}'.format(self.__get_login()[0], self.__get_login()[1]))

    def __cache(self):
        try:
            __arquivo = open('login.txt')
            __pwd = __arquivo.readline().split(':')
            self.__set_login(__pwd[0], __pwd[1])
        except:
            return False


