a = float(input('Digite o cumprimento do segmento a: '))
b = float(input('Digite o cumprimento do segmento b: '))
c = float(input('Digite o cumprimento do segmento c: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não fazem um triângulo.')

if a == b and b == c:
    print('Será um triângulo equilátero!')

elif a == b or b == c or a == c:
    print('Será um triângulo isósceles!')

else:
    print('Todos os lados são diferentes!')