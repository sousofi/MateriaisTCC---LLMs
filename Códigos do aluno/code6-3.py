# Nome: Maria Roberta
# Matrícula: 125786
# Data:	31/09/25	   
# O usuário deve adivinhar o número sorteado


##############################################################################
import random     # importação da biblioteca de geração de números aleatórios  
while True: 
    linf = 1   # definição do limite inferior
    lsup = 100 # definição do limite superior
    print('\nSerá sorteado um número de 1 a 100 e você deverá descobrir qual...!')
    random.seed(0)    # inicialização fixa da semente de geração de números aleatórios
    sorteado = random.randint(linf, lsup) # sorteia um número entre 1 e 100 
##############################################################################

    palpites = 0
    # criar e inicalizar o contador de palpites com o valor 0 (zero)
    while True  :  # o True deve ter um break programado quando o jogador acertar
    # Ler 1 palpite 
        N = int(input(f'Qual é o seu palpite [{linf}, {lsup}]? '))
        palpites+=1 
        # validar o palpite lido - tem que estar no intervalo atual
        while N < linf or N > lsup :
            print(f'Palpite fora do intervalo [{linf}, {lsup}]')
            N = int(input(f'Qual é o seu palpite [{linf}, {lsup}]? '))
        else:
            if N == sorteado: 
                break 
            elif N<sorteado:
                print(f'Dica número {palpites}: o número sorteado é maior que {N}.')
                linf = N+1
            elif N > sorteado: 
                print(f'Dica número {palpites}: o número sorteado é menor que {N}.')
                lsup = N-1

# imprime o resultado, após sair do while True
print(f'\nNúmero sorteado: {sorteado}')
print(f'você acertou na sua {palpites}º tentativa')
# escreva o segundo print para informar o número de tentativas
i=input('deseja jogar outra vez ? (S/N)').upper()
print()
print('obrigado por jogar o nosso jogo!')

