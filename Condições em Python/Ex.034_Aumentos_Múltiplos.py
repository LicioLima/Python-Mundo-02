salário = float(input('Qual é o salário do funcionário? R$ '))
if salário <= 2.750:
    novo = salário + (salário * 10 /100)
else:
    novo = salário + (salário * 5 / 100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))