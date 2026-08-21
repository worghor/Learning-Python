string = 'ABCD'
lista = ['maria', 'helena', 1, 2, 3, 'eduarda']
tupla = 'pthon', 'é', 'legal'
salas = [
    ['MARIA', 'HELENA',],
    ['ELAINE', ],
    ['LUIZ', 'JOAO', 'EDUARDA', ],
]


# p, s, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista:
    # print(nome, end=' ')

print(*lista)
print(*string)
print(*tupla, end='\n\n')
print(*salas, sep='\n')