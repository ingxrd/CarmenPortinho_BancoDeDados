--# Cria a tabela da classe "cliente"

    CREATE TABLE clientes 
    (id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(100),
    endereco VARCHAR(150))



--# Cria a tabela da classe "fornecedor"

    CREATE TABLE fornecedores 
    (id_fornecedor INT PRIMARY KEY,
    nome VARCHAR(100),
    cnpj VARCHAR(14),
    endereco VARCHAR(150))



---# Cria a tabela da classe "produto"

    CREATE TABLE produtos 
    (id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    categoria VARCHAR(100),
    quantidade_estoque INT)



--# Cria a tabela da classe "transação"

    CREATE TABLE transacoes 
    (id_transacao INT PRIMARY KEY, ----chave primaria
    quantidade_estoque INT,
    data_hora TIMESTAMP,
    cliente_id INT,
    produto_id INT,
    fornecedor_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes (id_cliente), --chave estrangeira
    FOREIGN KEY (produto_id) REFERENCES clientes (id_produto), --chave estrangeira
    FOREIGN KEY (fornecedor_id) REFERENCES clientes (id_fornecedor)) --chave estrangeira


