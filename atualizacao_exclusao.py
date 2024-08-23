import sqlite3

conexao = sqlite3.connect(r'banco_mercado.db')
cursor = conexao.cursor()

# Ativando as chaves estrangeiras (foreign keys)
cursor.execute('PRAGMA foreign_keys = ON;')


# Atualização tabela "cliente"
cursor.execute('UPDATE Clientes SET telefone = "987654" WHERE nome = "João Sousa"') 

#Atualização tabela "produto"
cursor.execute('UPDATE Produtos SET quantidade_estoque = 15 WHERE id_produto = 3 ')


conexao.commit()
conexao.close()
