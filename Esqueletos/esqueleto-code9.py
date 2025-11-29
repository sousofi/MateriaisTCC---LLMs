# coding: utf-8

# Nome do aluno:
# Matrícula:
# Data:
# Substitua esta linha por um breve comentáro dizendo o que o programa faz 

import numpy as np   # importa a biblioteca numpy

m = n = int(input('Informe a dimensão da matriz [2, 10]: '))
while m < 2 or m > 10 : # verifica dimensão do arranjo
    print('A dimensão deve ser entre 2 e 10')
    m = int(input('Informe a dimensão da matriz [2, 10]: '))

# cria um arranjo com N valores inteiros no intervalo [linf, lsup]
A = np.zeros((m, n))

# Escreva o código para preencher o arranjo A




    
# imprime o arranjo A após preenchimento
print('\nArranjo A:')
for i in range (0, m) :
    for j in range (0, n): 
        print(f'{A[i][j]:5.1f} ', end='')  # imprime 1 elemento com 1 casa decimal
    print() # pula para a próxima linha

# criar e preencher o arranjo B




# imprime o arranjo B após preenchimento
