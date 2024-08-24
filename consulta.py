import sqlite3

conexao = sqlite3.connect(r'banco_mercado.db')
cursor = conexao.cursor()


#Listar todos os produtos em estoque.
dados = cursor.execute('SELECT * FROM Produtos WHERE quantidade_estoque > 0;')
for produto in dados:
    print(f'Produtos em estoque: {produto}')

#Encontrar as vendas realizadas por um cliente específico.
def encontrar_vendas_por_cliente(cursor, cliente_id):
    dados = cursor.execute('SELECT * FROM transacoes WHERE cliente_id = ?;', (cliente_id,))
    for transacao in dados:
        print(f'Vendas do cliente {cliente_id}: {transacao}')

#Calcular o total de vendas por categoria de produto.
def calcular_total_vendas_por_categoria(cursor):
    dados = cursor.execute('''
        SELECT produtos.categoria, SUM(transacoes.quantidade_estoque * produtos.preco) AS total_vendas
        FROM transacoes
        JOIN produtos ON transacoes.produto_id = produtos.id_produto
        GROUP BY produtos.categoria;
    ''')
    
    for categoria, total_vendas in dados:
        print(f'Categoria: {categoria}, Total de Vendas: {total_vendas}')

#Identificar os produtos mais vendidos.
def identificar_produtos_mais_vendidos(cursor):
    dados = cursor.execute('''
        SELECT produtos.nome_produto, COUNT(transacoes.produto_id) AS total_vendas
        FROM transacoes
        JOIN produtos ON transacoes.produto_id = produtos.id_produto
        GROUP BY produtos.nome_produto
        ORDER BY total_vendas DESC;
    ''')
    
    for nome_produto, total_vendas in dados:
        print(f'Produto: {nome_produto}, Total de Vendas: {total_vendas}')

        
# Encontrar as vendas realizadas por um cliente específico.
encontrar_vendas_por_cliente(cursor, 1)

# Calcular o total de vendas por categoria de produto.
calcular_total_vendas_por_categoria(cursor)

# Identificar os produtos mais vendidos.
identificar_produtos_mais_vendidos(cursor)

conexao.close()


