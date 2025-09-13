soma = 0

print('A soma de todos os números divisíveis por três entre 1 e 500 é: ')

for n in range(1, 500, 2):
    if n % 3 == 0:
        soma += n
print(soma)
