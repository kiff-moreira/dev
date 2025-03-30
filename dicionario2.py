# Faça um programa que peça o nome e 3 notas de um aluno, essas informações devem ser salvas em um dicionário com as chaves "nome" e "notas" (notas deve ser uma lista com as 3 notas).

aluno = {}
notas = []

nome = input(' Digite o nome: ')

for n in range(3):
    nota = float(input(f' Digite a {n+1}º nota: '))
    notas.append(nota)

aluno={
    "nome": nome,
    "notas": notas
}


print(f' Nome {aluno.get("nome")}')
for nota in aluno.get("notas"):
    print(f' Notas {nota}')

