import sqlite3

def bd():
# Criando/Conectando ao Banco de Dados e o Cursor
    data = sqlite3.connect('bd.sqlite')
    cur = data.cursor()

    # Criando as Tabelas e os Usuários Padrão (Caso não existam).

    cur.executescript('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        nome TEXT,
        nascimento TEXT,
        tel TEXT,
        rg TEXT,
        ctps TEXT,
        endereco TEXT,
        cidade TEXT,
        admissao TEXT,
        obra_id INTEGER
    );
    
    CREATE TABLE IF NOT EXISTS Vales (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        funcionario_id INTEGER,
        valor INTEGER,
        data VARCHAR(10)
    );
    
    CREATE TABLE IF NOT EXISTS Faltas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        funcionario_id INTEGER,
        falta INTEGER,
        data VARCHAR(10)
    );
    
    CREATE TABLE IF NOT EXISTS Ferias (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        funcionario_id INTEGER,
        inicio VARCHAR(10),
        fim VARCHAR(10)
    );        
    
    CREATE TABLE IF NOT EXISTS Mural (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        mensagem TEXT,
        status INTEGER,
        destinatario_id INTEGER
    );
    
    CREATE TABLE IF NOT EXISTS Requisicoes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        obra_id INTEGER,
        user_id INTEGER,
        fornecedor_id INTEGER,
        material TEXT,
        valor INTEGER,
        informacao TEXT
    );
            
    CREATE TABLE IF NOT EXISTS Obras (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        nome VARCHAR(30),
        rua TEXT,
        numero INTEGER,
        bairro TEXT,
        cidade TEXT,
        telefone TEXT,
        contato TEXT,
        cei TEXT
    );
    
    CREATE TABLE IF NOT EXISTS Fornecedores(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        nome TEXT,
        endereco TEXT,
        tel TEXT,
        contato TEXT,
        descricao TEXT
    );
    
    CREATE TABLE IF NOT EXISTS Clientes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        nome VARCHAR(30),
        endereco TEXT,
        telefone VARCHAR(30),
        descricao TEXT
    );
    
    CREATE TABLE IF NOT EXISTS Receitas(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        cliente_id INTEGER,
        obra_id INTEGER,
        valor INTEGER,
        data VARCHAR(30),
        descricao TEXT
    );
    
    CREATE TABLE IF NOT EXISTS Despesas(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        obra_id INTEGER,
        valor INTEGER,
        data VARCHAR(30),
        venc VARCHAR(30),
        descricao TEXT
    );
        
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        grupo_id INTEGER,
        nome VARCHAR(30),
        senha TEXT
    );
    
    CREATE TABLE IF NOT EXISTS Grupo(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        nome VARCHAR(30)
    )
    ''')
    data.commit()
    if cur.execute('SELECT nome FROM Users').fetchone() == None:
        # Inserindo Grupos e Usuários Padrões, caso não existam.
        cur.executescript('''
            
            INSERT INTO Grupo(nome) VALUES('Administrador');
            
            INSERT INTO Grupo(nome) VALUES('Escritorio');
            
            INSERT INTO Grupo(nome) VALUES('Encarregado');
            
            INSERT INTO Grupo(nome) VALUES('Fornecedor');
                
            
            INSERT INTO Users(grupo_id, nome, senha) VALUES(1, 'adm', '123456');
            

        
        ''')

    data.commit()
    cur.close()
    print('Banco de Dados - OK')


