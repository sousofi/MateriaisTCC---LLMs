# Nome do aluno: Mara Silva
# Matrícula: 125478
# Data: 10/09/2025
# (breve comentário dizendo o que o programa faz)


nome=input('Nome: ')
idade = int(input('Idade atual: ') )
soma = idade
if idade >= 16 :
    print('\n%s, você pode jogar o campeonato pela idade: %d anos' %(nome, idade))
else:
    te = int(input('Tempo de Escolinha (TE): '))
    soma += te
    if te >= 5 :
        print('\n%s, você pode jogar o campeonato pelo TE: %d anos.' %(nome, te))
    elif te + idade >= 18 :
        print('\n%s, você pode jogar o campeonato pela soma (idade+TE): %d anos.' %(nome, idade+te))


        

