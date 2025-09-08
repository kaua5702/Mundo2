import time

produtos = {
    'camisa azul': 75.00,
    'camisa preta': 76.59,
    'camisa vermelha': 74.43,
    'camisa branca': 78.99

}

while True:

    print("\nProdutos disponíveis:")
    for item, preco in produtos.items():
        print(f"{item.title()}: R$ {preco:.2f}")
    escolha = input('\nQual item você vai levar? ').lower()

    if escolha in produtos:
        pgmt = print('Formas de pagamento: dinheiro, à vista cartão, 2x cartão e 3x no cartão. ')
        p = input('Qual a forma de pagamento? ').lower()
        if p == 'dinheiro':
            desc = 0.10
            total = (produtos[escolha]) - (produtos[escolha] * desc)
            print(f'O valor total ficou {total} reais')
            time.sleep(1)
            print('Insira o dinheiro')
            time.sleep(2)
            print('Processando...')
            time.sleep(4)
            print('Pagamento aprovado. Volte sempre!')
            time.sleep(1)
            break

        elif p == 'à vista cartão':
            desc = 0.05
            total = (produtos[escolha]) - (produtos[escolha] * desc)
            print(f'O valor total ficou {total} reais')
            time.sleep(1)
            print('Insira ou aproxime o cartão')
            time.sleep(3)
            print('Processando...')
            time.sleep(4)
            print('Pagamento aprovado. Volte sempre!')
            time.sleep(1)
            break
    
        elif p == '2x cartão':
            total = produtos[escolha]
            print(f'O valor total ficou {total} reais')
            time.sleep(1)
            print('Insira ou aproxime o cartão')
            time.sleep(3)
            print('Processando...')
            time.sleep(4)
            print('Pagamento aprovado. Volte sempre!')
            time.sleep(1)
            break

        elif p == '3x cartão':
            total = (produtos[escolha]) + (produtos[escolha] * 0.20)
            print(f'O valor total ficou {total} reais')
            time.sleep(1)
            print('Insira ou aproxime o cartão')
            time.sleep(3)
            print('Processando...')
            time.sleep(4)
            print('Pagamento aprovado. Volte sempre!')
            time.sleep(1)
            break

        else:
            print('Selecione uma opção válida')
            time.sleep(1)
            continue
    else:
        print('Produto não encontrado. Tente novamente.')
        continue

