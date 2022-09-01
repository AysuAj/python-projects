import enum
from random import randrange


print('-='*40)
print(' ')
print(f'{"JOGO DA FORCA":^40}')
print(' ')
print('-='*40)
print(' ')
print(' ')

palavra = str(input('Informe a palavra: '))
# divPalavra = palavra.split()
# listPalavra = list(divPalavra)
LARG_PALAVRA = len(palavra)
newPalavra = list()
listPalavra = list()

for elemento in palavra:
    listPalavra.append(elemento)

for elemento in range(0, LARG_PALAVRA):
    newPalavra.append('_')

print(f'A palavra tem {LARG_PALAVRA} letras.')

while True:
    print('Quer escolher uma letra ou falar a palavra?')
    choose = int(input('''
        1- Letra
        2- Palavra

        Escolha:  '''))

    if choose == 1:
        letra = str(input('Digite uma letra: '))
        for enum, elemento in enumerate(listPalavra):
            if letra == elemento:
                newPalavra.insert(enum, letra)
    
    elif choose == 2:
        digPalavra = str(input('Digite a palavra: '))
        if digPalavra == palavra:
            print('Voce acertou a palavra correta. Parabéns!!!')
            break
    
    print(' ')
    print('-- STATUS DA PALAVRA --')
    print(newPalavra)
    print(' ')
