# coding: utf-8

# Nome do aluno:
# MatrÃ­cula:
# Data:
# Substitua esta linha por um breve comentÃ¡rio dizendo o que o programa faz 

import numpy as np   # importa a biblioteca numpy

N = int(input('Informe o tamanho do arranjo: '))
while N < 15 or N > 25 : # verifica dimensão do arranjo
    print('O valor deve ser entre 15 e 25')
    N = int(input('Informe o tamanho do arranjo: '))
    
linf = 1  # limite inferior do intervalo [linf, lsup]
lsup = 20  # limite superior do intervalo [linf, lsup]

# TAREFA 1: ler e validar um nÃºmero inteiro
while True :
    semente = int(input('Informe o valor da semente (>=0): '))
    if semente >=0 :
        break
    print('Valor não pode ser negativo!')

# inicializa a semente para geraÃ§Ã£o de nÃºmeros pseudo-aleatÃ³rios  
np.random.seed(semente)

# cria um arranjo com N valores inteiros no intervalo [linf, lsup]
A = np.random.randint(linf,lsup+1, N)

# imprime o arranjo criado
print('\nArranjo A = [', end='')
for i in range (0, len(A)-1) :
    print(f'{A[i]}, ', end='')  # imprime 1 elemento de A seguido de 1 vírgula
print(f'{A[N-1]}]') # imprime o último, sem a vírgula depois

# ordena arranjo
for i in range (0, N-1) :
    # encontra o menor valor
    posMenor = i
    for j in range (i+1, len(A)):
        if A[j] < A[posMenor] :
            posMenor = j
    #troca
    A[i], A[posMenor] = A[posMenor], A[i]
  
# imprime o arranjo após a ordenação
print('\nA Ordenado = [', end='')
for i in range (0, len(A)-1) :  
    print(f'{A[i]}, ', end='')  # imprime 1 elemento de A seguido de 1 vírgula
print(f'{A[N-1]}]') # imprime o último, sem a vírgula depois

# Encontra a mediana
if N%2 == 0 :
    mediana = (A[N//2]+A[N//2-1])/2
    print(f'O valor da mediana é: ({A[N//2-1]}+{A[N//2]})/2 = {mediana:.1f}')
else :   
    mediana = A[N//2]
    print(f'O valor da mediana é: {mediana}')


