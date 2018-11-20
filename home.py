#coding: 'utf-8'

from comunicacao import WinComunicacao
from funcionarios import WinFuncionarios
from fornecedores import WinFornecedores
from comandos import *
from constantes import EMPRESA_NOME
from receitas import WinReceitas
from despesas import WinDespesas
from requisicoes import WinRequisicoes


class WinHome(object):

    def __init__(self):
        self.win = Tk()
        self.win.geometry('650x500+300+100')
        self.win.iconbitmap('icon.ico')
        self.win.title('ConstructorX - {}'.format(EMPRESA_NOME))
        self.win.iconbitmap('icon.ico')
        self.win.resizable(False, False)

        # FRAMES
        self.frame1 = Frame(self.win)
        self.frame2 = Frame(self.win)
        self.frame3 = Frame(self.win)
        self.frame4 = Frame(self.win)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        # IMAGENS
        self.img_receitas = picture('images/receitas.png')
        self.img_despesas = picture('images/despesas.png')
        self.img_requisicoes = picture('images/requisicoes.png')
        self.img_fornecedores = picture('images/fornecedores.png')
        self.img_funcionarios = picture('images/funcionarios.png')
        self.img_materiais = picture('images/materiais.png')
        self.img_obras = picture('images/obras.png')
        self.img_exames = picture('images/exames.png')
        self.img_comunicacao = picture('images/comunicacao.png')
        self.img_usuarios = picture('images/usuarios.png')
        self.img_administrador = picture('images/administrador.png')
        self.img_relatorios = picture('images/relatorios.png')

        # BOTÕES
        self.btn_receitas = Button(self.frame1, borderwidth=0, image=self.img_receitas, command=self.receitas).pack(padx=10, pady=10, side=LEFT)
        self.btn_despesas = Button(self.frame1, borderwidth=0, image=self.img_despesas, command=self.despesas).pack(padx=10, pady=10, side=LEFT)
        self.btn_requisicao = Button(self.frame1, borderwidth=0, image=self.img_requisicoes, command=self.requisicoes).pack(padx=10, pady=10, side=LEFT)
        self.btn_fornecedores = Button(self.frame1, borderwidth=0, image=self.img_fornecedores, command=self.fornecedores).pack(padx=10, pady=10, side=LEFT)
        self.btn_funcionarios = Button(self.frame2, borderwidth=0, image=self.img_funcionarios, command=self.funcionarios).pack(padx=10, pady=10, side=LEFT)
        self.btn_materiais = Button(self.frame2, borderwidth=0, image=self.img_materiais, command=self.materiais).pack(padx=10, pady=10, side=LEFT)
        self.btn_obras = Button(self.frame2, borderwidth=0, image=self.img_obras, command=self.obras).pack(padx=10, pady=10, side=LEFT)
        self.btn_exames = Button(self.frame2, borderwidth=0, image=self.img_exames, command=self.exames).pack(padx=10, pady=10, side=LEFT)
        self.btn_comunicacao = Button(self.frame3, borderwidth=0, image=self.img_comunicacao, command=self.comunicacao).pack(padx=10, pady=10, side=LEFT)
        self.btn_usuarios = Button(self.frame3, borderwidth=0, image=self.img_usuarios, command=self.usuarios).pack(padx=10, pady=10, side=LEFT)
        self.btn_administrador = Button(self.frame3, borderwidth=0, image=self.img_administrador, command=self.administrador).pack(padx=10, pady=10, side=LEFT)
        self.btn_relatorios = Button(self.frame3, borderwidth=0, image=self.img_relatorios, command=self.relatorios).pack(padx=10, pady=10, side=LEFT)


        self.win.mainloop()
        '''
        self.btn_receitas.pack(side=LEFT)
        self.btn_despesas.pack(side=LEFT)



        for x in range(len(BOTOES_MENU_HOME)):
            if x % 3 == 0:
                subframe = Frame(self.frame1)
                subframe.pack(side=LEFT)
            #b = botao(subframe, BOTOES_MENU[x])
            b2 = Button(subframe, text=BOTOES_MENU_HOME[x])
            b2.pack()'''

    def receitas(self):
        print('Acessando Receitas')
        return WinReceitas()

    def despesas(self):
        print('Acessando Despesas')
        return WinDespesas()

    def requisicoes(self):
        print('Acessando Requisições')
        return WinRequisicoes()

    def fornecedores(self):
        print('Acessando Fornecedores')
        return WinFornecedores()

    def funcionarios(self):
        print('Acessando Funcionários')
        WinFuncionarios()

    def materiais(self):
        pass

    def obras(self):
        pass

    def exames(self):
        pass

    def comunicacao(self):
        print('Acessando janela de Comunicação')
        return WinComunicacao()

    def usuarios(self):
        pass

    def administrador(self):
        pass

    def relatorios(self):
        pass

    def img_bg(self, nome):
        win['bg'] = Imagetk.PhotoImage(Image.open('images/layout/{}.jpg'.format(nome)))

