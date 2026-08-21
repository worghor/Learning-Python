lista = ['maria', 'joao', 'luiz']
lista.append('rafael')

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

            #ou

for indice, nome in enumerate(lista): #faz a mesma coisa que o decima (simplificação do python)
    print(indice, nome)