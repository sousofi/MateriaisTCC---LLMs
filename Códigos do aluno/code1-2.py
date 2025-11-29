# Nome do aluno: Bruna Souza
# Matrícula: 144657
# Data: 27/08/2025
# O programa identifica a idade e em qual periodo o aluno entrou na UFV. 

# ano atual
anoAtual = 2025
nome = input ('\nQual o seu nome?') 
ano = int(input ('Em que ano você nasceu?'))
curso = input ('Qual o seu curso?')
anoInicioDoCurso = int(input('Em que ano você iniciou seu curso?'))

idade = anoAtual - ano
periodo = (anoAtual-anoInicioDoCurso ) *2+2
idadeDeEntradaNoCurso = anoInicioDoCurso - anoAtual

print(f'\n{nome}, você está no {periodo}° periodo de {curso}.\nVocê tem {idade-1} ou {idade}.\nE entrou na UFV com {idadeDeEntradaNoCurso-1} ou {anoInicioDoCurso - ano}.')
