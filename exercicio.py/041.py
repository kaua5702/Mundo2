ano = 2025
nasc = int(input('Digite seu ano de nascimento: '))
idade = ano - nasc

if idade <= 9:
    print('Sua categoria é a mirim!')

elif idade <= 14 and idade > 9:
    print('Sua categoria é a infantil!')

elif idade <= 19 and idade > 14:
    print('Sua categoria é a junior!')

elif idade <= 20 and idade > 19:
    print('Sua categoria é a senior!')

else:
    print('Sua categoria é a master!')