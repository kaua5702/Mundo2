n = int(input('Digite um número inteiro: '))

if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print('Esse número não é primo')
            break
    else:
        print('Esse número é primo')
else:
    print('Esse número não é primo')
