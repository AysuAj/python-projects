nome = str(input('Informe o nome do funcionário: '))

valid = True
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

acum = 0
for i in meses:
        salario_mes = float(input(f'Informe o salário do mes {i}: R$'))
        acum += salario_mes

print(f'O valor total recebido no ano pelo funcionário {nome} foi de R${acum:.2f}')