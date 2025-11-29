# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o que o programa faz)


nome=input('Nome: ')
idade = int(input('Idade atual: ') )
if idade >= 16 :
    print('\n%s, você pode jogar o campeonato pela idade: %d anos' %(nome, idade))
else:
    te = int(input('Tempo de Escolinha (TE): '))
    if te >= 5 :
        print('\n%s, você pode jogar o campeonato pelo TE: %d anos.' %(nome, te))
    elif te + idade >= 18 :
        print('\n%s, você pode jogar o campeonato pela soma (idade+TE): %d anos.' %(nome, idade+te))
    else:
        print('\n%s, você ainda não pode jogar o campeonato!' %nome)
