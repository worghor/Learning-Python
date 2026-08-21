salas = [
    ['MARIA', 'HELENA',],
    ['ELAINE', ],
    ['LUIZ', 'JOAO', 'EDUARDA', ],
]

# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
