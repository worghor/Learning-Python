nome = "rafael santiago"
tamanho_nome = len(nome)
x = 0
nova_string = ""

while x < tamanho_nome:
    nova_string += '*' + nome[x]
    x += 1
    
nova_string += '*'
print(nova_string)
