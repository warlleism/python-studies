# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in mat[0]:
#     print(i, end=" ")

# for i in mat:
#     for i in i:
#         print(i, end=" ")


matriz = []

for i in range(1, 4):
    list = []

    while len(matriz) < 4:
        number = int(input('Digite um número: '))
        list.append(number)

        if len(list) == 4:
            matriz.append(list)
            list = []
            print('Lista Adicionada!')

print(matriz)
print('//////////')

for i in matriz:
    print(f'Lista: {i}')
    print(f'Maior valor: {max(i)}')
    print('//////////')
