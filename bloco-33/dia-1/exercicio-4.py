class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.quantidade = 0

    def pedir_item(self, qtn):
        self.quantidade += qtn


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.total_a_pagar = 0

    def add_item(self, itens):
        for item in itens:
            self.itens.append(item)

    def mostrar_pedido(self):
        for item in self.itens:
            print({item.quantidade, item.nome, item.preco})

    def mostrar_total_a_pagar(self):
        for item in self.itens:
            self.total_a_pagar += item.preco * item.quantidade

        print(self.total_a_pagar)


coca_cola = Item("coca cola", 5.50)
coxinha = Item("coxinha", 4.50)
cafe = Item("Café", 2.40)


coca_cola.pedir_item(2)
coxinha.pedir_item(2)
cafe.pedir_item(1)


pedido_pedro = Pedido("Pedro")
pedido_pedro.add_item([coca_cola, coxinha, cafe])

pedido_pedro.mostrar_pedido()
pedido_pedro.mostrar_total_a_pagar()