


letras = {}

texto = input(' Digite uma frase: ').upper()

"""for i in texto:
    if i in letras:
        letras[i] += 1 
    else:
        letras[i] = 1

print(letras)"""




for caractere in texto:
    if letras.get(caractere) is None:
        letras[caractere] = 1
    else:
        letras[caractere] +=1 


print(letras)