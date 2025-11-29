# coding: utf-8

# Autor: Anônimo
# Data: 20/9/2025
# Este programa mostra uma forma de implementar comando repetitivo que
# executa no mínimo 1 vez e com o número de repetições definida pelo usuário

i = 1
while i != 0 : # teste feito para obrigar a entrar na primeira vez

    # início do codigo do programa 
    print(f'\nMensagem número: {i}')
    # fim do codigo do programa

    # pergunta se o usuário quer executar outra vez
    resposta = input('Imprimir outra mensagem? (S/N): ').upper()
    if resposta == 'S' :
        # incrementa o valor de i
        i = i + 1
    else :
        # define o valor de i para parar o comando repetitivo
        i = 0
          
