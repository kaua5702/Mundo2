import time

print(' ')
print('  Bem vindo a nossa aba de emprestimo imobiliário!!\n')
time.sleep(0.7)
print('\33[0;36m=-=\33[0;36m' *20)
time.sleep(0.5)
print('Requisito\n ')
time.sleep(1)
print('Renda ser maior que 30 porcento da prestação\n')
time.sleep(1)
print('=-=' *20)
time.sleep(0.5)
print(' ')
time.sleep(1)

while True:
    valor = float(input('\033[mDigite o valor da casa: \033[m'))
    time.sleep(1)
    salario = float(input('Digite seu salário: '))
    time.sleep(1)
    anos = float(input('Em quantos anos deseja pagar?  '))
    time.sleep(1)
    valor_p = salario * 0.30
    prestacao = valor / (anos * 12)
    if prestacao > valor_p:
        print('Calculando...')
        time.sleep(3)
        print(f'O valor das parcelas ficaria {prestacao} reais')
        time.sleep(1)
        print('Emprestimo negado!\n')
        time.sleep(1)
        resposta = input('Deseja tentar novamente? (s/n) ')
        time.sleep(1)
        if resposta == 's':
            continue
        else:
            print('Encerrando...')
            time.sleep(2)
            break
    else:
        print(f'O valor das parcelas ficaria {prestacao}')
        time.sleep(1)
        print('Emprestimo aprovado!!')
        time.sleep(1)
        print('Encerrando...')
        time.sleep(2)
        break