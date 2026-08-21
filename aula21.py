#nomes = ['maria', 'joao', 'luiz']
# #nome1, nome2, nome3 = nomes


nome1, nome2, nome3 = ['maria', 'joao', 'luiz']
print(nome2)


nome, *resto = ['maria', 'joao', 'luiz']
print('\n', nome, resto)

_, _, nome, *resto = ['maria', 'joao', 'luiz']
print('\n', nome, resto)