print('{:^100}'.format(' LOJAS MARTINS '))
preço = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro / débito
[ 2 ] À vista no pix
[ 3 ] Até 3x no cartão de crédito
[ 4 ] Até 6x ou mais no cartão de crédito
''')
opção = int(input('QUal será sua forma de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 3
    print('Sua compra será parcelada em 3x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = 0
    print('Opção INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))