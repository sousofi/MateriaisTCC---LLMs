# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o que o programa faz)

# ano atual
anoAtual = 2025


nome = input('\nQual o seu nome? ')
ano = int(input('Em que ano você nasceu? '))
curso = input('Qual o seu curso? ')
inicio = int(input('Em que ano você iniciou seu curso? '))
periodo = (anoAtual-inicio)*2+2
idade = anoAtual - ano
idadeEnt = idade - (anoAtual - inicio)        
print('\n%s, você está no %dº período de %s.' %(nome,periodo,curso))
print('Você tem %d ou %d anos' %(idade-1, idade))
print('E entrou na UFV com %d ou %d anos.' %(idadeEnt-1, idadeEnt))

