dicionario = {}

nome = input(' Nome: ')
altura = input(' Altura: ')
idade = int(input( ' Idade: '))

dicionario = {
    "nome": nome,
    "Altura": altura,
    'Idade': idade
}
    

print('\n')
print(f' Nome {dicionario.get(nome)}')
print(f' altura {dicionario.get(altura)}')
print(f' Idade {dicionario.get(idade)}')

