num = int(input('Digite um número para calcular seu Fatorial: '))
c = num
f = 1
while c > 0:
    print(f'{c} x', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1

print(f'O fatorial de {num} é {f}')