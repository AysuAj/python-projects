import enum


palavra = 'samambaia'
newPalavra = ''

print('-='*40)
print(' ')
print(f'{"JOGO DA FORCA":^40}')
print(' ')
print('-='*40)
print(' ')
print(' ')

LARG_PALAVRA = len(palavra)

print(f'A palavra tem {LARG_PALAVRA} letras.')

while True:
    print('Quer escolher uma letra ou falar a palavra?')
    choose = int(input('''
        1- Letra
        2- Palavra

        Escolha:  '''))

    if choose == 1:
        letra = str(input('Digite uma letra: '))
        for elemento in palavra:
            if letra == elemento:
                    newPalavra += elemento
                    pass
                
            else:
                newPalavra += '_'
    
    elif choose == 2:
        digPalavra = str(input('Digite a palavra: '))
        if digPalavra == palavra:
            print('Voce acertou a palavra correta. Parabéns!!!')
            break
    
    print(' ')
    print('-- STATUS DA PALAVRA --')
    print(newPalavra)
    print(' ')
