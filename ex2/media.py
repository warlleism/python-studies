def calcular_media(notas):
    return sum(notas) / len(notas)


def obter_notas():
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f'Digite {i + 1}ª nota: '))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Por favor, digite uma nota entre 0 e 10.")
            except ValueError:
                print("Por favor, digite um número válido.")
    return notas


notas = obter_notas()
resultado = calcular_media(notas)

print(f'Resultado Média: {resultado:.1f} ')
