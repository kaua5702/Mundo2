n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Reprovado!')

elif media < 6.9 and media > 5.0:
    print('Você ficou de recuperação!!')

else:
    print('Aprovado!!!')