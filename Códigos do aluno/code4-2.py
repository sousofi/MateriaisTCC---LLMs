# # coding: utf-8

# Nome: Gabriel Fernandes
# Matrícula: 123456
# Data: 18/08/2025
# (breve comentário dizendo o que o programa faz)
# O código recebe a idade e verifica se os alunos podem ou não participar do campeonato
nome = input('nome: ')
idade = int(input('idade: '))
soma = 0
if idade >= 16:
   print('\n%s, você pode jogar o campeonato pela idade: %d anos' %(nome, idade))
else:
    tempo_escolinha = int(input('tempo de escolinha: '))
    if tempo_escolinha >= 5:
       print('\n%s, você pode jogar o campeonato pelo TE: %d anos.' %(nome, tempo_escolinha))
       soma = tempo_escolinha + idade
    elif soma >= 18:
       print('\n%s, você pode jogar o campeonato pela soma (idade+TE): %d anos.' %(nome, idade+tempo_escolinha))
    else:
       print('\n%s, você ainda não pode jogar o campeonato!' %nome)


        
    
