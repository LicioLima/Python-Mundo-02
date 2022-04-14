soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999: #Isso aqui é um flag!
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')