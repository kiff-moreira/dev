# Depois, calcule a média do aluno e sua situação (APROVADO se a nota for maior ou igual a 6, se não reprovado) e armazene essas informações em 2 novas chaves

alunos = {}
notas = []

nome = input(' Digite o nome: ')

for n in range(3):
    nota = float(input(f' Digite a {n+1}º nota: '))
    notas.append(nota)

alunos = {
    "nome": nome,
    "notas": notas
}

media = sum(notas) / len(notas)

print(f'nome {alunos.get('nome')}')
if media >= 6 :
    print(f' O aluno {alunos.get('nome')} esta APROVADO com meida {media:.2f}')
else:
    print(f' O aluno {alunos.get('nome')} esta REPROVADO com meida {media:.2f}')
