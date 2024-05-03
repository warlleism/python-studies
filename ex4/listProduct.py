carrinho = []

while True:
    price = input('Digite o preço do produto (ou "sair" para finalizar)')
    
    if price.lower() == 'sair':
        break
    
    name = input('Digite o nome do produto: ')
    qtd = input('Digite a quantidade de produtos: ')
    
    produto = {
        'price': price,
        'name': name,
        'qtd': qtd
    }
    
    carrinho.append(produto)
    print("Produto adicionado ao carrinho.")
    
print("Produtos no carrinho:")
itens = map(lambda x: x, carrinho)
lista = list(itens)
print(lista)
    
    