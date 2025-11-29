# Nome: 
# Matrícula:
# Data:		   
# Escreva aqui um breve comentário sobre o programa solução d 
#
#

##############################################################################
import random     # importação da biblioteca de geração de números aleatórios  
linf = 1   # definição do limite inferior
lsup = 100 # definição do limite superior
print('\nSerá sorteado um número de 1 a 100 e você deverá descobrir qual...!')
random.seed(0)    # inicialização fixa da semente de geração de números aleatórios
sorteado = random.randint(linf, lsup) # sorteia um número entre 1 e 100

##############################################################################


while True :
    # inicalizar o contador de palpites
    cont = 0
    while True  :  # o True deve ter um break programado quando o jogador acertar
        # Ler 1 palpite
        N = int(input(f'Qual é o seu palpite [{linf}, {lsup}]? '))
        # validar o palpite lido
        while N < linf or N > lsup :
            print(f'Palpite fora do intervalo [{linf}, {lsup}]')
            N = int(input(f'Qual é o seu palpite [{linf}, {lsup}]? '))
        # incrementar o contador de palpites
        cont = cont + 1
        # analisar o palpite do usuário
        if N == sorteado :
            # palpite certo!!! quebra o while-True
            break
        elif N > sorteado :
            # errou! atualiza o limite superior
            print(f'Dica número {cont}: o número sorteado é menor que {N}.')
            lsup = N-1
        else : # errou! atualiza o limite inferior
            print(f'Dica número {cont}: o número sorteado é maior que {N}.')
            linf = N+1
        

     
    # imprime o resultado, após sair do while True
    print(f'\nNúmero sorteado: {sorteado}')
    print(f'Você acertou na {cont}a tentativa')
    resp = input('Deseja jogar outra vez? (S/N): ').upper()
    if resp == 'S' :
        linf = 1   # definição do limite inferior para o próximo jogo
        lsup = 100 # definição do limite superior para o próximo jogo
        sorteado = random.randint(linf, lsup) # sorteia um número entre 1 e 100
        print('\nNovo número entre 1 a 100 foi sorteado e você deverá descobrir qual...!')
    else :
        break
print('\nObrigado por experimentar o nosso jogo!')




                
