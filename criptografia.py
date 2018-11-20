# encoding: 'utf-8'

from random import randint

__caracteres = 'abcdefghijklmnopqrstuvxywv0123456789ИСРПОНМЛКЙѢѡѠўѝќћњљјїіѕєѓђёѐяюэьыъщ'

def __encrypt(conteudo):
    global indice
    conteudo = str(conteudo)
    indice = 0 if 30 - len(conteudo) <= 0 else 30 - len(conteudo) - 1
    criptografado = ''
    if len(conteudo) < 30:
        for s in range(30-len(conteudo)):
            criptografado += __caracteres[randint(0, len(__caracteres)-1)]
        print(criptografado)
    for x in conteudo[::-1]:
        criptografado += chr(ord(x) + 360)
    print('\nCriptografia de "{}": {}'.format(conteudo, criptografado))
    return criptografado

def __decrypt(conteudo):
    descriptografado = ''
    for x in str(conteudo):
        for y in x[:indice:-1]:
            descriptografado += chr(ord(y) - 360)
    print('Descriptografado: ', descriptografado)
    return descriptografado

__decrypt(__encrypt('Renan'))



