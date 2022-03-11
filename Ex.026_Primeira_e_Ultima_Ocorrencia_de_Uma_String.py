frase = str(input('Digite uma frase: ')).upper()
print('A letra O aparece {} vezes na frase: '.format(frase.count('O')))
print('A primeira letra O apareceu na posição {}'.format(frase.find('O')+1))
print('A última letra O apareceu na posição {}'.format(frase.rfind('O')+1))