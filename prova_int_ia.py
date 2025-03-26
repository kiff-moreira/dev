# Programa para calcular média de alunos e verificar aprovação

# Solicita o número de alunos
num_alunos = int(input("Digite o número de alunos: "))

# Lista para armazenar os dados de todos os alunos
turma = []
soma_geral = 0

# Loop para cada aluno
for i in range(num_alunos):
    print(f"\nAluno {i+1}:")
    nome = input("Nome do aluno: ")
    
    # Solicita as 3 notas
    notas = []
    for j in range(3):
        nota = float(input(f"Digite a nota {j+1}: "))
        notas.append(nota)
    
    # Calcula a média do aluno
    media = sum(notas) / len(notas)
    soma_geral += media
    
    # Verifica aprovação
    situacao = "Aprovado" if media >= 7.0 else "Reprovado"
    
    # Armazena os dados do aluno
    aluno = {
        'nome': nome,
        'notas': notas,
        'media': media,
        'situacao': situacao
    }
    turma.append(aluno)

# Exibe os resultados individuais
print("\nResultados individuais:")
for aluno in turma:
    print(f"\n{aluno['nome']}:")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")

# Calcula e exibe a média geral
media_geral = soma_geral / num_alunos
print(f"\nMédia geral da turma: {media_geral:.2f}")