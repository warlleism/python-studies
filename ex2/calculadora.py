try:
    while True:
        num1_input = input("Digite o primeiro valor: ")
        try:
            num1 = float(num1_input)  # Permitir apenas números
            break
        except ValueError:
            print("Digite um número válido.")

    while True:
        try:
            operation = input("Qual operação deseja fazer (+, -, *, /): ")
            if operation not in ["+", "-", "*", "/"]:
                raise ValueError("Operação inválida")
            else:
                break
        except Exception as ve:
            print(ve)

    while True:
        num2_input = input("Digite o segundo valor: ")
        try:
            num2 = float(num2_input)  # Permitir apenas números
            if operation == "/" and num2 == 0:
                raise ValueError("Erro: Divisão por zero não é permitida.")
            else:
                break
        except ValueError:
            print("Digite um número válido.")

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None,
    }

    result = operations[operation](num1, num2)

    if result is None:
        print("Erro: Divisão por zero.")
    else:
        print("Resultado:", result)


except Exception as e:
    print("Ocorreu um erro não esperado:", e)
