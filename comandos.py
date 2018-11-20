#coding: 'utf-8'

from tkinter import *
from PIL import Image, ImageTk

# CRIADOR DE TÍTULOS
def criar_titulos(titulos, janela, sticky=E):
    row = 1
    for x in range(len(titulos)):
        label = Label(janela, text=titulos[x], pady=5)
        label.grid(row=row, column=1, sticky=sticky, padx=10)
        row += 1


def picture(linkdaimagem, tamanho=0):
    imagem = Image.open(linkdaimagem)
    if tamanho > 0:
        imagem = imagem.resize((tamanho, tamanho), Image.ANTIALIAS)
    imagem = ImageTk.PhotoImage(imagem)
    return imagem

