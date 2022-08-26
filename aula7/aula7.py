string = 'teste de strings'

new_string = ''
for letra in string:
    if letra == 'e':
        letra = '1'
    new_string+=letra
print(new_string)