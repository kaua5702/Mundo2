import time

print('  Bem vindo ao programa de conversão!!\n')
time.sleep(1)
numero = int(input('Digite um número inteiro: '))
time.sleep(1)

while True:
    print('[1] Binário')
    time.sleep(1)
    print('[2] Octal')
    time.sleep(1)
    print('[3] Hexadecimal')
    time.sleep(1)
    print('[4] sair')
    time.sleep(1)
    resposta = input('Selecione uma das opções para a conversão ou sair: ')
    if resposta == '1':
        print(f'{numero} em binário fica:')
        time.sleep(1)
        print(bin(numero)[2:])
        time.sleep(1)
        opcao = input('Deseja tentar outra opção? (s/n) ').lower()
        time.sleep(1)
        if opcao == 's':
            print('Carregando...')
            time.sleep(3)
            continue
        else:
            opcao2 = input('Ok. Deseja tentar outro número? (s/n) ').lower()
            time.sleep(1)
            if opcao2 == 's':
                print('Carregando...')
                time.sleep(1)
                while True:
                    try:
                        numero = int(input('Digite outro número: '))
                        time.sleep(1)
                        break
                    except ValueError:
                        print('Entrada inválida! Por favor, digite um número inteiro.')
                        time.sleep(1)
            else:
                print('Ok, encerrando...')
                time.sleep(3)
                break
    elif resposta == '2':
        print(f'{numero} em octal fica:')
        time.sleep(1)
        print(oct(numero)[2:])
        time.sleep(1)
        opcao = input('Deseja tentar outra opção? (s/n) ').lower()
        time.sleep(1)
        if opcao == 's':
            print('Carregando...')
            time.sleep(3)
            continue
        else:
            opcao2 = input('Ok. Deseja tentar outro número? (s/n) ').lower()
            time.sleep(1)
            if opcao2 == 's':
                print('Carregando...')
                time.sleep(1)
                while True:
                    try:
                        numero = int(input('Digite outro número: '))
                        time.sleep(1)
                        break
                    except ValueError:
                        print('Entrada inválida! Por favor, digite um número inteiro.')
                        time.sleep(1)
            else:
                print('Ok, encerrando...')
                time.sleep(3)
                break
    elif resposta == '3':
        print(f'{numero} em hexadecimal fica:')
        time.sleep(1)
        print(hex(numero)[2:])
        time.sleep(1)
        opcao = input('Deseja tentar outra opção? (s/n) ').lower()
        time.sleep(1)
        if opcao == 's':
            print('Carregando...')
            time.sleep(3)
            continue
        else:
            opcao2 = input('Ok. Deseja tentar outro número? (s/n) ').lower()
            time.sleep(1)
            if opcao2 == 's':
                print('Carregando...')
                time.sleep(1)
                while True:
                    try:
                        numero = int(input('Digite outro número: '))
                        time.sleep(1)
                        break
                    except ValueError:
                        print('Entrada inválida! Por favor, digite um número inteiro.')
                        time.sleep(1)
            else:
                print('Ok, encerrando...')
                time.sleep(3)
                break
    elif resposta == '4':
        print('Ok, volte sempre!')
        time.sleep(1)
        print('Encerrando...')
        time.sleep(3)
        break
    
    else:
        print('Opção inválida. Tente novamente.')
        continue
