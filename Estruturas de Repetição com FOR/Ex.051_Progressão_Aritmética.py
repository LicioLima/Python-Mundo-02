primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for i in range(primeiro, décimo, razão):
    print(f'{i}', end=' → ')
print("IT'S OVER!")