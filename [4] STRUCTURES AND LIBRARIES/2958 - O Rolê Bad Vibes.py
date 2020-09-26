'''
A faculdade é um tempo memorável da vida. Grandes coisas acontecem, mas também muita dor e sofrimento, e nesses momentos bons amigos são necessários.
Sabendo disso, Úrisson, ao entrar na universidade, tratou logo de fazer bons amigos e fundar seu grupo de ajuda, Rolê Bad Vibes, o qual os membros se ajudam com problemas de disciplinas do curso e de vida.
Como são um grupo de pessoas muito inteligentes, bolaram um esquema para resolução dos problemas:
Para cada problema, era dado um valor de 1 a 9 (na escala de criticidade), e uma letra, D ou V, indicando problema de disciplina ou de vida, respectivamente. Com esses dados, colocam em uma matriz, impressa em uma grande cartolina colada na sede do grupo para fácil visualização de todos.
A matriz é uma boa forma de visualizar, porém, ainda causa confusão na hora de escolher os problemas a serem resolvidos no dia, pois os dados ficam muito esparsos. Assim, Úrisson gostaria de gerar um relatório, ordenado desses dados.
O critério adotado é: independente da criticidade, os problemas de vida devem ser resolvidos primeiro, pois concluíram ser muito complicado conciliar esses problemas com os problemas de disciplinas. Depois, basta ordenar por criticidade.
Úrisson, pediu pra você, veterano de programação, criar um programa que gera este relatório.

Entrada
A primeira linha da entrada contém dois inteiros N e M, indicando, respectivamente, o número de linhas e colunas. Nas próximas linhas, é dada a matriz onde cada célula contém dois caracteres, o primeiro indicando o nível de criticidade e o segundo se é um problema de vida ou disciplina.

Saída
Relatório ordenado conforme pedido por Úrisson.
'''

entrada = list(map(int, input().split()))
N = entrada[0]
M = entrada[1]

matriz = []

for i in range(N):
    linha = input().split()
    for l in linha:
        matriz.append(l)

matriz_vida = sorted([int(i[0]) for i in matriz if 'V' in i], reverse = True)
matriz_disciplina = sorted([int(i[0]) for i in matriz if 'D' in i], reverse = True)

for v in matriz_vida:
    print(f'{v}V')

for d in matriz_disciplina:
    print(f'{d}D')