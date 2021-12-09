# Como podemos abstrair um pedido composto por vários itens
#  em um sistema de vendas de uma cafeteria?
#  Qual seu nome, atributos e comportamentos?

class Cafeteria:
    def __init__(self, nome, endereco, funcionarios, produtos):
        self.nome = nome
        self.endereco = endereco
        self.funcionarios = funcionarios
        self.produtos = produtos


class Item:
    def __init__(self, produto, preco, quantidade):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade


class Venda:
    def __init__(self, vendedor, cliente, itens):
        self.vendedor = vendedor
        self.cliente = cliente
        self.itens = itens

    def atendimento(self):
        return [{'atendente': self.vendedor}, {'cliente': self.cliente}]

    def controle_de_produtos_por_pedido(self):
        return list({item.product: item.quantidade} for item in self.itens)

    def total_por_pedidos(self):
        return sum(list(item.preco * item.quantidade for item in self.itens))


cafeteria_1 = Cafeteria(
    'Vovó Delícia',
    'Casa de vovó',
    ['Patrícia', 'Miguel', 'Paula'],
    [{'broa': 2.5}, {'café': 1.5}, {'pão de quaijo': 2}, {'leite': 2}])


duas_broas = Item('broa', 2.5, 2)
tres_cafe = Item('café', 1.5, 3)

mesa_1 = Venda(cafeteria_1.funcionarios[2], 'Joana', [duas_broas, tres_cafe])
