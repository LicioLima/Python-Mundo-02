nome = str(input('Qual é o seu nome? '))
if nome == 'Lício':
    print('Que nome lindo! ^^')
elif nome == 'Lício' or nome == 'Carlos' or nome == 'Gevanésio':
    print('Nome diferenciado rochedo, parabéns!')
else:
    print('Que nome horrendo você tem!')
print('Tenha um bom dia, {}!'.format(nome))