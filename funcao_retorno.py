# Funcao retorno

def saudacao(nome = ""):
    if nome == '':
        return ' Ola '
    else:
        return f' Ola, {nome}'

nome = input(' Digite seu nome (<ENTER> caso nao queira informar): ')
mensagem = saudacao(nome)
print(mensagem)