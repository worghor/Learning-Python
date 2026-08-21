import os
lista_compras = []

while True:
    opcao = input('selecione um opção\n[i]nserir [a]pagar [l]istar [s]air: ')
    os.system('cls')

    if opcao == 'i':  
        lista_compras.append(input('Digite o nome da mercadoria: '))

    elif opcao == 'a':
        try:
            indice = int(input('Digite a mercadoria pelo indice que quer apagar: '))
            if indice <= len(lista_compras):
                lista_compras.pop(indice)

            else:
                ('indice invalido, item não apagado!')

        except ValueError:
            print('Não pode ser letra')

    elif opcao == 'l':
        if not lista_compras:
            print('Lista está zerada')

        else:
            for indice, mecadoria in enumerate(lista_compras):
                print(indice, mecadoria)

    elif opcao == 's':
        print('voce encerrou a lista!')
        break

    else:
        print('opção invalida!')

