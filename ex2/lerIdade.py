
while True:
    try:
        nome = input('Digite seu nome: ')
        if len(nome) == 0:
            print("Campo nome não pode ser vazio!")
        else:
            print(f'Seu nome é {nome}')
            break
    except Exception as error:
        print(error)
