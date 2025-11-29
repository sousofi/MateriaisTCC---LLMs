# coding: utf-8

# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o que o programa faz)

print('\nBem-vindo à Central de Ingressos do Play Center')
# Escreva seu código abaixo desta linha. 
nome = input('Nome: ')
idade = int( input('Idade: '))
if idade < 4 or idade >= 65 :
    valor = 0
    tipo = 'SEM ACESSO'
else :
    if idade < 13 :
        valor = 75
    elif idade < 18:
        valor = 85
    else:
        valor = 115
    altura = float(input('Altura (em metros): '))
    if altura < 1.50 :
        tipo = 'ACESSO RESTRITO'
        valor = 0.9*valor
    else:
        tipo = 'ACESSO TOTAL'
print(f'\n{nome}, seu ingresso custa R$ {valor:.2f}. Tipo: {tipo}.')
    




