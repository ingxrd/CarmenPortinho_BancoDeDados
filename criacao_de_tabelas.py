import sqlite3 

#fazendo a conexao com o banco de dados na mesma pasta do arquivo python
conexao = sqlite3.connect(r'banco_mercado.db')
cursor = conexao.cursor()


# Cria a tabela da classe "cliente"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes 
    (id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(100),
    endereco VARCHAR(150))
''')

# Confirma as mudanças no banco de dados
conexao.commit()


# Cria a tabela da classe "fornecedor"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS fornecedores 
    (id_fornecedor INT PRIMARY KEY,
    nome VARCHAR(100),
    cnpj VARCHAR(14),
    endereco VARCHAR(150))
''')

# Confirma as mudanças no banco de dados
conexao.commit()


# Cria a tabela da classe "produto"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos 
    (id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    categoria VARCHAR(100),
    quantidade_estoque INT)
''')

# Confirma as mudanças no banco de dados
conexao.commit()


# Cria a tabela da classe "transacao"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transacoes 
    (id_transacao INT PRIMARY KEY,
    quantidade_estoque INT,
    data_hora TIMESTAMP,
    cliente_id INT,
    produto_id INT,
    fornecedor_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes (id_cliente), 
    FOREIGN KEY (produto_id) REFERENCES clientes (id_produto), 
    FOREIGN KEY (fornecedor_id) REFERENCES clientes (id_fornecedor)) 
''')


# Confirma as mudanças no banco de dados
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()

