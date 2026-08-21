nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
texto = f"seu nome é: {nome} {sobrenome}\nseu imc é: {imc:.2f}"
print(texto)