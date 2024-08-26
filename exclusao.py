import sqlite3

conexao = sqlite3.connect(r'banco_mercado.db')
cursor = conexao.cursor

#cursor.execute('DELETE FROM cliente where endereco = "Paris"')

#cursor.execute('DELETE FROM produto where id_produto = "Nintendo Switch"')

conexao.commit()
conexao.close()
