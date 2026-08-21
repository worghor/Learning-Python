lista = ['maria', 'joao', 'luiz']
x = 0
lista.append('rafael')
for nome in lista:
    print(f'{x} - {nome}')
    x += 1

            # ou

lista = ['maria', 'joao', 'luiz']
lista.append('rafael')
indices = range(len(lista))
for indice in indices:
    print(indice,' - ', lista[indice])