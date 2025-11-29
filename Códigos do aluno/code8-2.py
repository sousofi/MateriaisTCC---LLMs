# coding: utf-8

# Nome do aluno: Matheus Jorge
# Matrícula: 236587
# Data: 22/10/2025
# O programa ordena um arranjo A e calcula a mediana dos elementos

import numpy as np  # importa a biblioteca numpy
# Ler e validar um número inteiro no intervalo [15, 25]
N = int(input('Informe o tamanho do arranjo: '))
while N < 15 or N > 25 : # verifica dimensão do arranjo
    print('O valor deve ser entre 15 e 25')
    N = int(input('Informe o tamanho do arranjo: '))    
# Ler e validar um número inteiro
while True :
    semente = int(input('Informe o valor da semente (>=0): '))
    if semente >=0 :
        break
    print('Valor não pode ser negativo!')
# inicializa a semente para geração de números pseudo-aleatórios [1, 100]  
np.random.seed(semente)

linf = 1  # limite inferior do intervalo [linf, lsup]
lsup = 100  # limite superior do intervalo [linf, lsup]
# cria um arranjo com N valores inteiros no intervalo [linf, lsup]
A = np.random.randint(linf,lsup+1, N)
# imprime o arranjo criado, com os valores separados por vírgulas
print('\nArranjo A = [', end='')
for i in range (0, len(A)-1) :
    print(f'{A[i]}, ', end='')  # imprime 1 elemento de A seguido de 1 vírgula
print(f'{A[N-1]}]') # sem a vírgula depois do último elemento
####################################################################
# complete o código a partir da linha 36 para implementar:         #
# - a ordenação dos elementos do arranjo A, em ordem crescente     #
# - a impressão do valor da mediana                                #
####################################################################
for i in range(len(A) - 1):           
    posicao_menor = i                 
    for j in range(i + 1, len(A)):
        if A[j] < A[posicao_menor]:
            posicao_menor = j
    A[i], A[posicao_menor] = A[posicao_menor], A[i]

print('\nArranjo A ordenado = [', end='')
for i in range(len(A) - 1):
    print(f'{A[i]}, ', end='')
print(f'{A[len(A) - 1]}]')

if N % 2 == 1:
    mediana = (A[N // 2 - 1] + A[N // 2]) / 2
else:
    mediana = A[N // 2]

print(f'\nO valor da mediana é: {mediana}')

    
