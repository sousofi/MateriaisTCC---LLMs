# coding: utf-8

# Nome do aluno:
# Matrícula:
# Data:
# Substitua esta linha por um breve comentário dizendo o que o programa faz 


import numpy as np   # importa a biblioteca numpy

N = 25    # dimensão do arranjo
linf = 0  # limite inferior do intervalo [linf, lsup]
lsup = 9  # limite superior do intervalo [linf, lsup]

# tarefa 1 do roteiro: ler e validar um número inteiro
semente = 0



# inicializa a semente para geração de números pseudo-aleatórios  
np.random.seed(semente)

# cria um arranjo com N valores inteiros no intervalo [linf, lsup]
A = np.random.randint(linf,lsup+1, N)

# imprime o arranjo criado
print('\nArranjo = [ ', end='')
for i in range (0, len(A)) :
    print(A[i], end=' ')
print(']')

# encontra a média inteira
soma = 0
for i in range (0, len(A)):
    soma = soma + A[i]
medint = soma // len(A)
print(f'Média inteira: {medint}')


# complete o código, abaixo desta linha, para implementar a tarefa 2
# descrita no roteiro

