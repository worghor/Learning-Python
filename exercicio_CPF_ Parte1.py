#Gerar o primeiro digito
#CPF a ser utilizado 427.314.889-72

# cpf_string = '11901813983'
# lista_cpf_digito = []
# lista_cpf_digito_10x = []
# multiplicador = 10
# digito = 0
# soma_9d_10x = 0
# calculo_primeiro_d = 0

# for indice in range(len(cpf_string)-2): #isso aqui ja faz +=
#     digito = int(cpf_string[indice])
#     lista_cpf_digito.append(digito) 
#     lista_cpf_digito_10x.append(lista_cpf_digito[indice]*multiplicador)
#     soma_9d_10x += lista_cpf_digito_10x[indice]
#     multiplicador -= 1

# calculo_primeiro_d = (soma_9d_10x * 10) % 11
# if calculo_primeiro_d == 10:
#    calculo_primeiro_d = 0


# print(lista_cpf_digito)
# print(lista_cpf_digito_10x)
# print(soma_9d_10x)
# print(calculo_primeiro_d)


# lista_cpf_digito.append(calculo_primeiro_d)
# multiplicador = 11
# indice = 0
# soma_10d_11x = 0

# for indice in range(len(lista_cpf_digito)):
#     soma_10d_11x += lista_cpf_digito[indice] * multiplicador
#     multiplicador -= 1

# soma_10d_11x = (soma_10d_11x * 10) % 11

# if soma_10d_11x == 10:
#    soma_10d_11x = 0

# print(soma_10d_11x)

# lista_cpf_digito.append(soma_10d_11x)

# lista_cpf_digito = ''.join(map(str, lista_cpf_digito))
# print(lista_cpf_digito)

# if cpf_string == lista_cpf_digito:
#     print('CPF valido')
# else:
#     print('invalido')


#Otimizado
cpf = '48100438609'
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

if cpf == cpf_valido:
    print(f'CPF {cpf} é valido')
else:
    print('CPF invalido')



