lista = []

for i in range(1, 6):
    el = float(input(f'Digite um numero {i}/5: '))
    lista.append(el)

media = sum(lista) / 5


for elem in lista:
    print(f' {int(elem)} ', end="")

print(f'Média: {media}')

listNumbers = []

while True:
    number = int(
        input('Digite um número: caso queira parar, basta digitar 0: '))
    if number == 0:
        print('Volte sempre!')
        break
    listNumbers.append(number)
