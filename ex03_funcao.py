def media(numeros):
    if len(numeros) == 0:
        return 0
    
    return sum(numeros) / len(numeros)

numeros = []

while True:
    numero = float(input(' Digite um numero: '))
    numeros.append(numero)
    
    sair = input(' Digite [N] para sair: ')
    if sair == 'N' or 'n':
        break
    
resultado = media(numeros)


print(f' A media das notas e {resultado}')