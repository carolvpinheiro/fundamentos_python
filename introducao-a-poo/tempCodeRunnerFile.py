class Cafeteria:
    def __init__(self, nome, endereco, funcionarios, produtos):
        self.nome = nome
        self.endereco = endereco
        self.funcionarios = funcionarios
        self.produtos = produtos

    def pedidos(self):
        print("Pedido realizado!")


class Venda:
    def __init__(self, vendedor, cliente, produto, preço, quantidade):
        self.vendedor = vendedor
        self.cliente = cliente
        self.produto = produto
        self.preço = preço
        self.quantidade = quantidade


cafeteria_1 = Cafeteria(
    'Vovó Delícia',
    'Casa de vovó',
    ['Patrícia', 'Miguel', 'Paula'],
    {'broa': 2.5, 'café': 1.5, 'pão de quaijo': 2, 'leite': 2})

cafeteria_1.pedidos
