# Nome: Ana Maria
# Matrícula: 245637
# Data: 10/09/2025
# (substitua essa linha por um comentário dizendo o que o programa faz)

# ano atual
anoAtual = 2025

nome = input('Qual o seu nome?: ')
nascimento = int(input('Quando você nasceu?: '))
curso = input('Qual o seu curso?: ')
ano_do_curso = int(input('Qual o ano de inicio do curso?: '))
                            
periodo = (((anoAtual - ano_do_curso)* 2) + 2)
idade = anoAtual - nascimento
ano_entrou = (ano_do_curso - nascimento)
print(f"{nome}, você está no {periodo} periodo do curso.")
print(f"Você tem {idade} ou {idade-1} anos e entrou na UFV com {ano_entrou} anos") 