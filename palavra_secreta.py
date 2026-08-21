# i = 0
# Palavra_secreta = 'perfume'
# ast_secreto = ['*', '*', '*', '*', '*', '*', '*']
# palavra_descoberta_parcial = ''

# while True:
#     letra_digitada = input("digite uma letra? ")
#     print(f'condigo secreto: {''.join(ast_secreto)}')
#     for i in range(len(Palavra_secreta)):
#         if letra_digitada == Palavra_secreta[i]:
#             ast_secreto[i] = letra_digitada
#             if '*' not in ast_secreto:
#                 print('Voce venceu parabens!!')

#Palavra_secreta = 'perfume'
#ast_secreto = ['*', '*', '*', '*', '*', '*', '*']

Palavra_secreta = input('digite uma palavra secreta: ')
ast_secreto = ['*'] * len(Palavra_secreta)
x = 0
i = 0

while True:

    print(f'condigo secreto: {''.join(ast_secreto)}')
    letra_digitada = input("digite uma letra? ")
    if len(letra_digitada) != 1:
        print("voce digitou mais de uma letra, não contabilizou nas tentativas") 

    for i in range(len(Palavra_secreta)):
        if letra_digitada == Palavra_secreta[i]:
            ast_secreto[i] = letra_digitada
    
    if letra_digitada != Palavra_secreta:
        print("nao tem essa letra!")
    x += 1
    if '*' not in ast_secreto:
        print('Voce venceu parabens!!')
        print(f"seu numero de tentativas foi {x}")
        break