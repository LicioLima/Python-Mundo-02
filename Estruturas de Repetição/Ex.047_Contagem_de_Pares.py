from time import sleep
for n in range (1,51):
    print('.', end='')
    sleep(0.1)
    if n% 2 == 0:
        print(n, end=' ')
print('ACABOU!')

