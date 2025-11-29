# coding: utf-8

# Nome do aluno: Miguel Pires
# Matrícula: 115749
# Data: 10/09/2025
# A idade e altura da pessoa define o valor e tipo de ingresso

print('\nBem-vindo à Central de Ingressos do Play Center')
# Escreva seu código abaixo desta linha. 
nome = input("Nome: ")
idade = int(input("Idade: "))

if idade < 4 or idade >= 65 :
    valor = 0
else :
    if idade < 13 :
        valor = 75
    elif idade < 18:
        valor = 85
    else:
        valor = 115

print(f'\n{nome}, seu ingresso custa R$ {valor:.2f}.')
