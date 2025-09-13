somaidade = 0
mediaidade = 0
mih = 0
hv = ''
totm20 = 0

for p in range(0, 4):
    print(f'----- {p}ª pessoa -----')
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: (m/f) ').strip()
    somaidade += 1
    if p == 1 and sexo in 'Mn':
        mih = idade
        hv = nome
    if sexo in 'Mn' and idade > mih:
        mhi = idade
        hv = nome
    if sexo in 'Fm' and idade < 20:
        totm20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho se chama {hv} e tem {mih} anos')
print(f'Ao todo são {totm20} com menos de 20 anos')