string = 'teste de strings'

new_string = ''
for letra in string:
    if letra == 'e':
        letra = '1'
    elif letra == 't':
        letra = '$'
    new_string+=letra
print(new_string)