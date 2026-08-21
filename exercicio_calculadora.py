while True:
    while True:
        primeiro_numero = (input('Digite o primeiro número: '))
        try:
            primeiro_numero = float(primeiro_numero)
            break
        except ValueError:
            print('Número inválido. Tente novamente.')
            continue

    while True:        
        segundo_numero = (input('Digite o segundo número: '))
        try:
            segundo_numero = float(segundo_numero)
            break
        except ValueError:
            print('Número inválido. Tente novamente.')
            continue
    while True:
        operador = input('Digite o operador (+, -, *, /): ')
        if operador in ['+', '-', '*', '/']:
            break
        else:
            print('Operador inválido. Tente novamente.')
            continue  

    if operador == '+':
        resultado = primeiro_numero + segundo_numero
        print(f"Resultado: {resultado}")
    elif operador == '-':
        resultado = primeiro_numero - segundo_numero
        print(f"Resultado: {resultado}")
    elif operador == '*':
        resultado = primeiro_numero * segundo_numero
        print(f"Resultado: {resultado}")
    elif operador == '/':
        resultado = primeiro_numero / segundo_numero
        print(f"Resultado: {resultado}")
    else:
        print('Operador inválido. Tente novamente.')
        continue

    print('Deseja realizar outra operação? (s/n)')
    saida = input()
    if saida == 'n':
        break
