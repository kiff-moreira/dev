import random

cadastro = []

nome = None
endereco = None
telefone = None
valor = None

while True:

    print('\n')
    resp = input(' Deseja realizar uma nova venda?  S ou N? ')
    print("\n")
    resp = resp.upper()

    if resp == "N":
        break
        print(' Fim do programa. ')

    nome = input(" Nome: ")
    endereco = input(' Endereço: ')
    telefone = input(' Telefone: ')
    valor = float(input(' Valor da compra: '))

    vendas = {"nome":nome, 
              "endereco":endereco, 
              "telefone":telefone, 
              "valor":valor
    }

    cadastro.append(vendas)


if cadastro == 0:
    print(' Nao foi registrada nenhuma venda hoje')

else:

    for vendas in cadastro:
        print('=' * 60)
        print(f' Nome:  {vendas.get(nome)}')
        print(f' Endereço: {vendas.get(endereco )}')
        print(f' Telefone: {vendas.get(telefone)}')
        print(f' Valar: {vendas.get(valor)}')
        print('=' * 60)
        print('\n')

    if cadastro:
        venda_sorteada = random.choice(cadastro)
        
        print(' '* 20, ' PARABENS ')
        print('=' * 60)
        print(" O cliente Sorteado foi ")
        print(f' Nome: {venda_sorteada.get(nome)}')
        print(f' Telefone: {venda_sorteada.get(telefone)}')
        print(f' Endereço: {venda_sorteada.get(endereco)}')
        print('=' * 60 )






