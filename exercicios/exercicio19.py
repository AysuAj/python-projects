import random

alunos = []
candidatos = int(input('Informe quantos alunos candidatos: '))
cont = 0

while cont < candidatos:
    aluno_nome = str(input('Informe o nome do aluno candidato: '))
    cont+=1

aluno_escolhido = random.choice(alunos)

print(f'O aluno escolhido para apagar o quadro foi {aluno_escolhido}!')
