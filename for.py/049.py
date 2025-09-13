n = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuada de {n} é')

for i in range(1, 11):
    print(f'{n} x {i} = {i*n}')