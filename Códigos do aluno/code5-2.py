# coding: utf-8

# Nome do aluno: Kaiki Lopes
# Matrícula: 142563
# Data:24/09/25
# Substitua estas 2 linhas por um breve comentário dizendo o que o 
# programa faz, após você ter concluído a terceira tarefa do roteiro

# msgs iniciais
print('Programa para cálculo das raízes de equação do 2o grau')
print('cuja fórmula geral é dada por: ax² + bx + c')
# mensagens específicas para uma equação
cont = 0
while cont == 0:
    print('Informe os valores dos coeficientes da equação')
    # Ler os coeficientes da equação
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    
    #calcular delta
    delta = b**2 - 4*a*c
    # primeira parte da resposta
    print(f'\nA equação {a:.3f}x² + {b:.3f}x + {c:.3f} = 0, ', end='')
    # testa todos os casos possíveis
    if a == 0 :  # não é de 2o. grau
        print('não é uma de 2⁰ grau, pois o coeficiente a = 0')
    elif delta < 0: # sem raízes reais
        print('não possui raízes reais')
    elif delta == 0:  # apenas 1 raiz real
        # calculo da raiz
        x1 = (-b - (delta)**0.5) / (2*a)
        # impressão do valor calculado
        print(f'possui uma única raiz real: {x1:.3f}')
    else : # 2 raízes reais
        # cálculo das raízes
        x1 = (-b - (delta)**0.5) / (2*a)
        x2 = (-b + (delta)**0.5) / (2*a)
        #imprimir os valores calculados para as 2 raízes
        print(f'possui duas raízes reais {x1:.3f} e {x2:.3f}')


    resposta=input('Deseja executar novamente? (S/N):  ').upper()
    if resposta == 'S':
        cont = 0
    else:
        cont += 1
    if resposta != 'S':
        break
   
