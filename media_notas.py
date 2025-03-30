notas = []

for n in range(3):
    nota = int(input(f' Digite a {n+1}º nota: '))
    notas.append(nota)

"""qtd_notas = len(notas)
for n in range(qtd_notas):
    print(f' A {notas[n]:}')"""



for nota in notas:
    print(f' - {nota}')

media = sum(notas) / len(notas)
print(f' A media é {media:.2f} ')
