numeros = [{'num': 1}, {'num': 2}, {'num': 3}]
quadrados = map(lambda x: x['num'], numeros)
quadrados = list(quadrados)
print(quadrados)  
