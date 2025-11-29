# Nome: Maria Souza
# Matrícula: 125784
# Data:	31/09/25	   
# Um número é sorteado e o operador deve tentar adivinhar como uma
# brincadeira de criança 


##############################################################################
import random     # importação da biblioteca de geração de números aleatórios  
linf = 1   # definição do limite inferior
lsup = 100 # definição do limite superior
print('\nSerá sorteado um número de 1 a 100 e você deverá descobrir qual...!')
random.seed(0)    # inicialização fixa da semente de geração de números aleatórios
sorteado = random.randint(linf, lsup) # sorteia um número entre 1 e 100 
##############################################################################

    # criar e inicalizar o contador de palpites com o valor 0 (zero)
palpites=0

while True:  # o True deve ter um break programado quando o jogador acertar
    # Ler 1 palpite 
    N = int(input(f'Qual é o seu palpite [{linf}, {lsup}]? '))
    # validar o palpite lido - tem que estar no intervalo atual
    while N<linf or N>lsup:
        print("Palpite fora do intervalo")
        N = int(input(f'Qual é o seu palpite [{linf}, {lsup}]? '))
        
    # incrementar o contador de palpites
    palpites=palpites+1
    
    # analisar o palpite do usuário para as 3 possibilidades:
    # 1) palpite certo - o while True deve ser quebrado (uso do break)
    # 2) palpite maior do que o número sorteado - o limite superior deve
    #    ser atualizado
    # 3) palpite menor do que o número sorteado - o limite inferior deve
    #    ser atualizado
    if N==sorteado:
        break
    elif N>sorteado:
        print(f'Dica número {palpites}: o número sorteado é menor.')
        lsup=N-1
    else:
        print(f'Dica número {palpites}: o número sorteado é maior.')
        linf=N+1

# imprime o resultado, após sair do while True
print(f'\nNúmero sorteado: {sorteado}')
# escreva o segundo print para informar o número de tentativas
print(f'Número de palpites: {palpites}')

# pergunta se deseja jogar outra vez
resposta = input("Deseja jogar outra vez? (S/N): ")
if resposta != "S":
    print("\nObrigado por experimentar o nosso jogo!")
   
