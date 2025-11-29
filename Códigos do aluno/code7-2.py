# coding: utf-8

# Nome do aluno: Mirian Silva
# Matrícula: 99578
# Data: 08/10/2025
# O código verifica se o valor digitado é maior que zero e vê a média dos 25 números do arranjo...
# ... e depois imprime os números maiores que a média.

import numpy as np   # importa a biblioteca numpy

N = 25    # dimensão do arranjo
linf = 0  # limite inferior do intervalo [linf, lsup]
lsup = 9  # limite superior do intervalo [linf, lsup]

# tarefa 1 do roteiro: ler e validar um número inteiro

while True:
    semente = int(input('Digite o valor da semente: '))

    if semente < 0:
        print('O valor da semente deve ser >= 0')
        semente = int(input ('Informe o valor da semente: ') )
    elif semente == 123: 
        break
    
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
    valores = 0

    for i in range(0, N):
        if A[i] > medint:
            valores += 1

    print(f'Existem {valores} maiores que a média inteira')
        








