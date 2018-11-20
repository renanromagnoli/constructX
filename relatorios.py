# encoding: 'utf-8'

def ver_obras():
    obras = list()
    with open('obras.txt', 'r') as f:
        for x in f.readlines():
            obras.append(x.split('_'))
    return obras

def ver_fornecedores():
    fornecedores = []
    with open('fornecedores.txt', 'r') as f:
        for x in f.readlines():
            fornecedores.append(x.split('_'))
    return fornecedores

def ver_funcionarios():
    funcionarios = []
    with open('funcionarios.txt', 'r') as f:
        for x in f.readlines():
            funcionarios.append(x)
    return funcionarios