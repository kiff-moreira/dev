# importando a bilbioteca para gerar o sorteio randomico (ALEATORIO)
import random


nome_cliente = None
endereco = None
tel = None
valor_compra = None

# criação de lista vazia para armazenar os cadastros
cadastro = []

while True:
    # solicitacao de dados para efetivar o cadastro
    print("\n")
    nome_cliente = input(' Nome: ')
    endereco = input(' Enderenço: ')
    tel = int(input(' Telefone: '))
    valor_compra = float(input(' Qual o valor da compra: '))
    print("\n")
    resp = (input('deseja registra outra venda? (S/N): '))
    print("\n")
    resp = resp.upper()

    #criação do cadastro do cliente
    meu_dicionario = {"nome_cliente":nome_cliente, "endereco":endereco, "tel":tel, "valor_compra": valor_compra,}

    # modo de adicionar o cadastro do dicionario na lista vazia
    cadastro.append(meu_dicionario)

    # verificação de continuidade do programa
    if resp == 'N':
        break

# imprimindo dados dos clientes na tela       
for meu_dicionario in cadastro:
    print("=" * 60 )
    print(f' Nome: {meu_dicionario["nome_cliente"]}')
    print(f' Endereço: {meu_dicionario['endereco']}')
    print(f' Telefone: {meu_dicionario['tel']}')
    print(f' Valor da compra: {meu_dicionario['valor_compra']}')
    print("=" * 60 )
    print("\n")

if cadastro:
    cliente_sorteado = random.choice(cadastro)
    print(" = " * 30 )
    print(" O CLIENTE SORTEADO FOI : ")
    print(f' Nome: {cliente_sorteado['nome_cliente']}')
    print(f' Endereço: {cliente_sorteado['endereco']}')
    print(f' Telefon: {cliente_sorteado['tel']}')
    print(" = " * 30 )
    print("\n")
    