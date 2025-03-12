contador = 0
acerto = 6


while True:
    print('\n Jogo de adivinhação, boa sorte! ')
    
    tentativas = int(input(' Digite um numero de 0 a 9 : '))
    print('\n')
    contador += 1
    
    if tentativas == acerto:
        print(f'\n Parabens você acertou o numero da sorte que é {acerto}')
        break

    elif contador == 3:
        print('\n É uma pena, nao foi desta vez... ')
        break
     
    else:
        print(f'\n Tente mais uma vez! ')