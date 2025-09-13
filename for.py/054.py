from datetime import date

maiores = 0
menores = 0
atual = date.today().year

for i in range(0, 7):
    nasc = int(input('Digite o ano de seu nascimento: '))
    if atual - nasc < 21:
        menores += 1
    else:
        maiores += 1
print(f'{menores} é menor de idade')
print(f'{maiores} é maior de idade')

