nome = input("Digite seu nome completo: ")
idade = input("Digite sua idade: ")
quantidade_letras = len(nome)

if idade and nome:
    print(f"seu nome é {nome}")
    print(nome[-1:(-quantidade_letras-1):-1])
    #print(nome[::-1]) <<<< de maneira simplificada

    if " " in nome:
        print("seu nome tem espaço")
    else:
        print("seu nome não tem espaço")

    print(f"seu nome tem {quantidade_letras} letras")
    print(f"a primeira letra doseu nome é : {nome[0]}")
    print(f"a última letra do seu nome é : {nome[-1]}")
else:
    print("Desculpe, você digitou um nome vazio ou uma idade negativa. Por favor, tente novamente.")
