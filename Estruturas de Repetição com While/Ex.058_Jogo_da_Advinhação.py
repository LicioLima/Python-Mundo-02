from random import randint
computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez CRIA')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print(f'Acertou com {palpites} tentativas. PARABUAINS!')