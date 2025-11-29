# coding: utf-8

# Nome do aluno: Armando Batista
# Matrícula: 528694
# Data: 03/09/2025

# mensagens iniciais
print('Este programa calcula a área e o perímetro de figuras regulares')
print('Escolha o tipo de figura (1 ou 2): ')
print('   Digite 1 para CÍRCULO')
print('   Digite outro valor para RETÂNGULO')
opcao = int(input('Digite a sua opção: '))


# cálculo da área de um círculo
if (opcao == 1):
    figura = 'Círculo'
    PI = 3.14159
    raio = float(input('Informe o raio do círculo (cm): ') )
    area = PI * raio ** 2
    perimetro = 2 * PI * raio
# cálculo da área de um retângulo
else:
    figura = 'Retângulo'
    print('Informe as dimensões retângulo (cm)')
    base = float(input('base = '))
    altura = float(input('altura = '))
    area = base * altura
    perimetro = 2 * (base + altura)

# imprime o resultado
print(f'\nA área da {figura} é: {area:.2f} cm².' )
print(f'O perímetro da {figura} é: {perimetro:.2f} cm.' )
