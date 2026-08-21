valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
if valor1 > valor2:
    print(f"O maior valor é o primeiro, que é {valor1}")
elif valor2 > valor1:
    print(f"O maior valor é o segundo, que é {valor2}")
else:
    print(f"Os valores são iguais, que é {valor1}") 