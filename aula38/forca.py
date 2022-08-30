import enum


palavra = 'samambaia'
newPalavra = ''
while True:
    print('-='*40)
    print(' ')
    print(f'{"JOGO DA FORCA":^40}')
    print(' ')
    print('-='*40)
    print(' ')
    print(' ')

    LARG_PALAVRA = len(palavra)
    newPalavra = '_'*LARG_PALAVRA

    print(f'A palavra tem {LARG_PALAVRA} letras.')
    print('Quer escolher uma letra ou falar a palavra?')
    choose = int(input('''
        1- Letra
        2- Palavra
        Escolha:  '''))

    if choose == 1:
        letra = str(input('Digite uma letra: '))
        for elemento in palavra:
            if elemento == letra:
                    elemento+=newPalavra
                
            else:
                newPalavra+= '_'
    
    print(newPalavra)