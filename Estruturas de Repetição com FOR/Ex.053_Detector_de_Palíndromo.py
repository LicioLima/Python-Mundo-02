frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''. join(palavras)
inverso = junto[::-1]
print(f'o inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')