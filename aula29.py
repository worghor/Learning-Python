import random
import sys
import os

somador_invalidos = 0
nove_digitos = ''
tentavtivas = 1
while True:
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))
        somador_invalidos += 1

    cpf = nove_digitos
    soma = 0
    multiplicador = 10


    for indice in cpf[0:9]:
        soma += int(indice) * multiplicador
        multiplicador -= 1

    primeiro_digito = (soma * 10) % 11

    if primeiro_digito == 10:
        primeiro_digito = 0

    cpf2 = cpf[0:9] + str(primeiro_digito)
    multiplicador = 11
    soma2 = 0

    for indice2 in cpf2:
        soma2 += int(indice2) * multiplicador
        multiplicador -= 1

    segundo_digito = (soma2 * 10) % 11

    if segundo_digito == 10:
        segundo_digito = 0

    cpf_valido = cpf[0:9] + str(primeiro_digito) + str(segundo_digito)

    if cpf == cpf:
        print(f'{tentavtivas} CPF {cpf_valido}')
        nove_digitos = ''
        tentavtivas += 1
        if tentavtivas == 101:
            break
