# Nome do aluno: Bárbara Silveira
# Matrícula: 144659
# Data: 27/08/2025
# O programa fala idade, perído e qual período de ingresso do aluno na UFV. 

# ano atual
anoAtual = 2025
nome = input ('\nDigite seu nome:') 
ano = int(input ('Digite seu ano de nascimento:'))
curso = input ('Digite seu curso:')
inicio = int(input('Digite o ano de ingresso no curso:'))

periodo = (anoAtual-inicio)*2+2
idade = anoAtual - ano
entrada = inicio - anoAtual 

print(f'\n{nome}, você está no {periodo}° periodo de {curso} e entrou na UFV com {entrada-1} ou {inicio - ano}.')
