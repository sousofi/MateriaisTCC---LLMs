# # coding: utf-8

# Nome: Cássio Pereira
# Matrícula:125478
# Data:17/09/25
# O programa define condições para solucionar um problema.

nome=input('Digite seu nome:')
idade=int(input('Digite: sua idade atual:'))
tempo=int(input('Digite quanto tempo de  escolinha você tem:'))

if idade>=16:
    print(f'{nome} você pode jogar o campeonato pela idade: {idade} anos')
elif tempo>=5:
    print(f'{nome} você pode jogar o campeonato pelo TE: {tempo} anos')
elif tempo+idade>18:
    print(f'{nome} você pode jogar o campeonato pela soma: {tempo + idade} anos')
else:
    print(f'{nome} você ainda não pode jogar o campeonato')
    
