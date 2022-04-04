número = int(input('digite um número: '))
tot = 0
for i in range(1, número + 1):
    if número % i == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')
print(f'o número {número} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')