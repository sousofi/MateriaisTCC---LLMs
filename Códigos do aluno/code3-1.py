# coding: utf-8

# Nome do aluno: Bianca Andrade
# Matrícula: 101457
# Data: 10/09/2025
# (breve comentário dizendo o que o programa faz)
# O programa gerencia o acesso ao parque de acordo com idade e altura

print('\nBem-vindo à Central de Ingressos do Play Center')
# Escreva seu código abaixo desta linha. 
nome = input('Nome: ')
idade = int(input('Idade: '))
altura = float(input('Altura: '))

if idade < 4 or idade >= 65:
      ingresso = 0.00
      tipo_acesso = 'SEM ACESSO'
else:
      if idade < 13:
         ingresso = 75.00
      elif idade < 18:
         ingresso = 85.00
      elif idade >= 18:
         ingresso = 115.00
if altura < 1.50:
   ingresso = ingresso * 0.9
if altura < 1.50:
    tipo_acesso = 'ACESSO RESTRITO'
else:
    tipo_acesso = 'ACESSO TOTAL'
    
print(f'{nome}, seu ingresso é do tipo{tipo_acesso} e o valor é R${ingresso}.')    
