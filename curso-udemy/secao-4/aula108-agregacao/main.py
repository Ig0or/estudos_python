from classes import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Tenis', 300)
p3 = Produto('Caneca', 12)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(f"Total: R${carrinho.soma_total():.2f}")

