import sqlite3

conexao = sqlite3.connect(r'banco_mercado.db')
cursor = conexao.cursor()

#selecionar todas as informacoes da tabela usuario onde o nome desse usuario esteja tambem dentro da tabela gerentes
#dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerente)')
#for usuario in dados:
#   print(usuario)

#Listar todos os produtos em estoque.
dados = cursor.execute('SELECT * FROM Produtos WHERE quantidade_estoque > 0;')
for produto in dados:
    print(f'Produtos em estoque: {produto}')

#Encontrar as vendas realizadas por um cliente específico.
dados2 = cursor.execute('SELECT * FROM transacoes WHERE cliente_id = 1;')
for transacao in dados2:
    print(f'Vendas do cliente: {transacao}')

#Calcular o total de vendas por categoria de produto.

#Identificar os produtos mais vendidos.
