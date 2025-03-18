def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    sequencia = [0,1]
    n = 0

    while n < numero:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
        n += 1

    return sequencia

print(" " * 10, " SEQUENCIA FIBONACCI ")
numero = int(input('Digite quantos numeros da sequecia quer ver: '))

print(fibonacci(numero))
