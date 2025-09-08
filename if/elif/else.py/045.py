import random
import time

pc = random.randint(1, 3)
usuario = int(input('Digite 1 para pedra, 2 para papel ou 3 para tesoura: '))
time.sleep(1)
print(f'O computador escolheu {pc}')
time.sleep(1)

if pc == usuario:
    print('Empate!')
    time.sleep(1)

elif (usuario == 1 and pc == 3) or \
     (usuario == 2 and pc == 1) or \
     (usuario == 3 and pc == 2):
    print('Você venceu!')

else:
    print('O computador venceu!')
    time.sleep(1)