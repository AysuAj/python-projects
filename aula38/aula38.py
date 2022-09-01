from random import randrange


palavra = str(input('Informe a palavra: '))
divPalavra = palavra.split(',')
listPalavra = list(divPalavra)
LARG_PALAVRA = len(palavra)
newPalavra = list()

for elemento in range(0, LARG_PALAVRA):
    newPalavra.append('_')

print(newPalavra)