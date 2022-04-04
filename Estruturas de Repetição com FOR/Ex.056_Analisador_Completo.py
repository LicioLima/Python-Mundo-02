somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulher20 = 0
for i in range(1, 4):
    print(f'————— {i}ª PESSOA —————')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaIdade = somaIdade / 3
print(f'A média de idade do grupo é de {mediaIdade} anos')
print(f'O homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
