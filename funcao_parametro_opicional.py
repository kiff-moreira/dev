# Podemos tornar um valor opicional definindo um valor para ele


def saudacao(nome=''):
    if nome == "":
        print(' Ola')
    else:
        print(f'OLA, {nome}')


saudacao()
saudacao(' Kiff ')