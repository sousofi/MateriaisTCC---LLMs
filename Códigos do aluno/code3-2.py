# coding: utf-8

# Nome do aluno: Caio Pires
# Matrícula: 115747
# Data: 10/09/2025
# ( Dependendo da idade e altura
# é definido o acesso aos brinquedos)

print('\nBem-vindo à Central de Ingressos do Play Center')
# Escreva seu código abaixo desta linha. 
nome = input("Nome: ")
idade = int(input("Idade: "))
tipo = "SEM ACESSO"
valor = 0

if idade >= 4 and idade <= 12:
    valor = 75.00
elif idade >= 13 and idade <= 17:
    valor = 85.00
elif idade >= 18 and idade <= 65:
    valor = 115.00
else:
    valor = 0
    
if idade <= 64:
    altura = float(input(" Altura (em metros):"))
    if altura < 1.5:
        valor = valor * 0.9
        tipo = "ACESSO RESTRITO"
    else:
        tipo = "ACESSO TOTAL"
                   
print(f'{nome}, seu ingresso custa R$ {valor:.2f} Tipo: {tipo}')





