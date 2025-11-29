# coding: utf-8

# Nome do aluno: Carla Márcia
# Matrícula: 526487
# Data: 10/11/2025
# O programa confere quantos números são maiores do que a média dos valores de um array


import numpy as np   # importa a biblioteca numpy

N = 25    # dimensão do arranjo
linf = 0  # limite inferior do intervalo [linf, lsup]
lsup = 9  # limite superior do intervalo [linf, lsup]

# tarefa 1 do roteiro: ler e validar um número inteiro
semente = int(input ('Informe o valor da semente: ') )
while semente < 0 :
    print('O valor da semente deve ser >= 0')
    semente = int(input ('Informe o valor da semente: ') )


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
cont = 1
for i in range (1, len(A)) :
    if A[i] >= medint:
        cont = cont + 1
print(f'Existem {cont} valores maiores que a média inteira.')

