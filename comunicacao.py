#conding = 'utf-8'

from tkinter import *
from comandos import picture

class WinComunicacao(object):
    def __init__(self):

        self.win = Toplevel()
        self.win.geometry('500x320+400+200')
        self.win.title('Mural de Recados')
        self.win.iconbitmap('icon.ico')
        self.win.resizable(False, False)

        self.img_enviar = picture('images/send.png', 40)

        self.ls_mural = Listbox(self.win, width=80, height=15)
        self.tit_mensagem = Label(self.win, text='Mensagem: ')
        self.mensagem = Entry(self.win, width=50)
        self.btn_enviar = Button(self.win, image=self.img_enviar, borderwidth=0, command=self.enviar)
        self.btn_enviar.image = self.img_enviar

        self.ls_mural.grid(row=1, column=1, padx=10, pady=10, columnspan=3)
        self.tit_mensagem.grid(row=2, column=1, sticky=E)
        self.mensagem.grid(row=2, column=2)
        self.btn_enviar.grid(row=2, column=3)

        self.win.mainloop()

    def enviar(self):
        self.ls_mural.insert(0, '{}: {}'.format('Renan', self.mensagem.get()))
        self.mensagem.delete(0, 'end')

