from random import random


import random

lista_alunos = []
candidato = int(input('Informe quantos candidatos: '))
cont = 0

while cont < candidato:
    aluno_nome = str(input('Informe o nome do aluno candidato: '))
    lista_alunos.append(aluno_nome)
    cont+=1

elementos = len(lista_alunos)
alunos_sorteados = []
for elemento in range(0, elementos):
    new_el = random.choice(lista_alunos)
    alunos_sorteados.append(new_el)
    lista_alunos.remove(new_el)

print('Ordem de apresentação:')
for enum, e in enumerate(alunos_sorteados):
    print(f'    {enum+1}- {e}')
