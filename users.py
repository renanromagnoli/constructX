#coding: utf-8

import datetime as dt

class Usuario(object):

    def __init__(self, nome, grupo=0):
        self.__id = None
        self.__nome = nome
        self.__senha = str()
        self.__grupo = grupo
        self.__msg_recebidas = []
        self.__msg_ = []
'''
    def send_msg(self):
        self.msg_data = dt.date.today().strftime('%d/%m/%y')
        self.msg_hora = dt.time().strftime('%H:%M:%S')
        self.msg_remetente = self.id
        self.msg_texto = input('Mensagem: ')
        with open('mensagens.txt', 'w') as m:
            m.write('{} | {} | {} | Texto:{}\n'.format(self.msg_remetente, self.msg_data, self.msg_hora, self.msg_texto))
'''




