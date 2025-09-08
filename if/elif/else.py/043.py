import time

print('Bem vindo(a) a calculadora de IMC\n')
time.sleep(0.7)

p = float(input('Digite seu peso(kg): '))
time.sleep(1)
al = float(input('Digite sua altura(m): '))
time.sleep(1)
calculo = p / (al * al)

if calculo < 18.5:
    print('Você esta abaixo do peso!')
    time.sleep(1)

elif calculo >= 18.5 and calculo <= 25:
    print('Você está com o peso ideal!!')
    time.sleep(1)

elif calculo >= 25 and calculo <= 30:
    print('Você está com sobrepeso!')
    time.sleep(1)

elif calculo >= 30 and calculo <= 40:
    print('Você está com obesidade!')
    time.sleep(1)

else:
    print('Você está com obesidade mórbida!')
    time.sleep(1)