from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opcao = int(input('→→→ Qual é a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação entre {n1} * {n2} é {multiplicacao}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
             maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novameente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando... ')
    else:
        print('Opção inválida. Tente Novamente!')
    print('=-=' * 10)
    sleep(3)
print('Fim do programa! Volte sempre!')