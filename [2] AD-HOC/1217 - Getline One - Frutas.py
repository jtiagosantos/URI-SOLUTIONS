'''
Dona Parcinova, mãe de Mangojata, pediu a ela que ajudasse a calcular o consumo de frutas da casa e a quantidade gasta por dia nestas frutas. Mangojata agora deve então fazer um programa a partir de uma tabela que sua mãe estava utilizando para anotações há quase um ano. Nesta tabela, dona Parcinova anotou a quantidade de dias e depois o valor gasto cada dia e as frutas compradas naquele dia, sempre na quantidade de um KG por tipo de fruta.

Entrada
A primeira linha de entrada contém um inteiro N (1 ≤ N ≤ 365) que indica o número de casos de teste que vem a seguir. Cada caso de teste é composto por 2 linhas. A primeira linha contém um valor de ponto flutuante V (0.10 ≤ V ≤ 20.00) indicando o valor gasto no dia e a segunda linha contém o nome de cada uma das frutas que dona Parcinova comprou.

Saída
Para cada caso de teste, imprima quantos kg de frutas dona Parcinova comprou em cada dia, com mensagem correspondente em inglês, conforme exemplo abaixo. No final, apresente o consumo médio em kg por dia com 2 casas decimais seguido da mensagem correspondente e a média de gasto por dia com as frutas, também em inglês e com mensagem correspondente, conforme o exemplo abaixo.

Obs.: Todas as letras da saída devem ser impressas em minúsculas, com exceção do "R" de "R$"
'''

N = int(input())
gastos = []
kg = []
for i in range(N):
    gastos.append(float(input()))
    entrada = str(input()).split()
    kg.append(len(entrada))
for k,v in enumerate(kg):
    print('day {}: {} kg'.format(k+1, v))
print('{:.2f} kg by day'.format(sum(kg)/N))
print('R$ {:.2f} by day'.format(sum(gastos)/N))
