# coding: utf-8

# Nome do aluno: Carla Maria
# Matrícula: 235748
# Data: 30/10/25
# São duas matrizes quadradas: a primeira com valores
# da linha e coluna e a segunda com valores definidos pela diagonal principal.

import numpy as np   # importa a biblioteca numpy

m = n = int(input('Informe a dimensão da matriz [2, 10]: '))
while m < 2 or m > 10 : # verifica dimensão do arranjo
    print('A dimensão deve ser entre 2 e 10')
    m = int(input('Informe a dimensão da matriz [2, 10]: '))

# cria um arranjo com N valores inteiros no intervalo [linf, lsup]
A = np.zeros((m, n))

# Escreva o código para preencher o arranjo A

for i in range(m):
    for j in range(n):
        A[i][j] = i + 0.1*j
    
# imprime o arranjo A após preenchimento
print('\nArranjo A:')
for i in range (0, m) :
    for j in range (0, n): 
        print(f'{A[i][j]:5.1f} ', end='')  # imprime 1 elemento com 1 casa decimal
    print() # pula para a próxima linha

# criar e preencher o arranjo B

B = np.zeros((m, n), dtype=int)
for i in range(m):
    for j in range(n):
        if i == j:
            B[i][j] = 0
        else:
            if i < j:
                B[i][j] = 2+i + j
            else:
                B[i][j] = i + 2*j


# imprime o arranjo B após preenchimento

print('\nArranjo B:')
for i in range(m):
    for j in range(n):
        print(f'{B[i][j]:5d}', end='')
    print()
