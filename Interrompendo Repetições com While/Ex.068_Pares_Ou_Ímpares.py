from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()
    print(f'Você jogou{jogador} e o computador{computador}. Total de {total}', end=' ')
    print('DEU PAR if total %2 == 0 else')
    if tipo == 0:
        if total % 2 == 0:
            print('Você VENCEU! ')
            v += 1
        else:
            print('Você PERDEU! ')
            break
    elif tipo == 'I':
        print('Você perdeu! ')
        break
    print('Vamos jogar novamente.... ')
print(f'GAME OVER! Você venceu {v} vezes')
