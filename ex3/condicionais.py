

while True:
    nota = float(input('Digite a nota: '))
    if nota >= 7:
        print('Aprovado(a)')
        break
    elif nota < 7.0 and nota >= 4:
        print('Recuperação')
        break
    elif nota < 4:
        print('Reprovado(a)')
        break

itens = [1, 2, 3, 4, 5]

while True:
    numero = float(input('Digite um número: '))

    if numero in itens:
        print('Valor existente')
        break
    else:
        print('Valor não existente')
        break


itens2 = [1, 2, 3, 4, 5]

while True:
    numero = float(input('Digite um número: '))

    if numero not in itens2:
        print('Valor não existente')
    else:
        print('Valor existente')
