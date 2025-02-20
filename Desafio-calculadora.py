def Calculadora():
    while True:
        print("Calculadora Simples:")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        operation = input("Selecione uma opção ou 's' para sair: ")

        if operation == 's' or operation == 'S':
            print("Obrigado por utilizar a Calculadora Simples.")
            break

        if operation not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("Segundo número: "))

        if operation == '1':
            result = numero_1 +  numero_2
            print("O result da operação soma é: ", result)
        elif operation == '2':
            result = numero_1 - numero_2
            print("O result da operação subtração é: ", result)
        elif operation == '3':
            result = numero_1 * numero_2
            print("O result da operação multiplicação é: ", result)
        else:
            if numero_2 == 0:
                print("Divisões por zero não são possíveis. Tente novamente.")
                continue
            else:
                result = numero_1 / numero_2
                print("O result da operação divisão é: ", result)

Calculadora()