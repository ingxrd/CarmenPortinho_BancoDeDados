from gerenciamento_mercado.mercado import Mercado
from gerenciamento_mercado.cliente import Cliente
from gerenciamento_mercado.fornecedor import Fornecedor
from gerenciamento_mercado.produto import Produto
from gerenciamento_mercado.transacao import Transacao

# Exemplo de transação no mercado
if __name__ == "__main__":
    mercado = Mercado()

    cliente = Cliente("Carmen Portinho", "123456789", "Rua Pedro Pires, 123")
    mercado.adicionar_cliente(cliente)

    fornecedor = Fornecedor("Nestlé", "Av. Paulista, 125", "77.377.074/0001-76")
    produto = Produto("Arroz", [fornecedor], "Alimentos", 25)
    mercado.adicionar_produto(produto)

    transacao = Transacao(cliente, produto, 2)  # Certifique-se de que o cliente está antes do produto
    mercado.registrar_transacao(transacao)

    # Imprimindo dados para verificar o sistema rodando corretamente
    print("Cliente:")
    print(cliente)

    print("\nFornecedor:")
    print(fornecedor)

    print("\nTransação:")
    print(transacao)
