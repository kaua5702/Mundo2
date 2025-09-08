ano = 2025
nasc = int(input('Digite seu ano de nascimento: '))
idade = ano - nasc
temp = 18 - idade

if idade == 18:
    print('Esta na hora de se alistar!')

elif idade < 18:
    print(f'Falta {temp} ano(s) para você se alistar!')

else:
    print(f'Você já devia ter se alistado a {(-1) * temp} ano(s)')