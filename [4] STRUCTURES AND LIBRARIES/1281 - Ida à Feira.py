'''
Dona Parcinova costuma ir regularmente à feira para comprar frutas e legumes. Ela pediu então à sua filha, Mangojata, que a ajudasse com as contas e que fizesse um programa que calculasse o valor que precisa levar para poder comprar tudo que está em sua lista de compras, considerando a quantidade de cada tipo de fruta ou legume e os preços destes itens.

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1281.png

Entrada
A primeira linha de entrada contém um inteiro N que indica a quantidade de idas à feira de dona Parcinova (que nada mais é do que o número de casos de teste que vem a seguir). Cada caso de teste inicia com um inteiro M que indica a quantidade de produtos que estão disponíveis para venda na feira. Seguem os M produtos com seus preços respectivos por unidade ou Kg. A próxima linha de entrada contém um inteiro P (1 ≤ P ≤ M) que indica a quantidade de diferentes produtos que dona Parcinova deseja comprar. Seguem P linhas contendo cada uma delas um texto (com até 50 caracteres) e um valor inteiro, que indicam respectivamente o nome de cada produto e a quantidade deste produto.

Saída
Para cada caso de teste, imprima o valor que será gasto por dona Parcinova no seguinte formato: R$ seguido de um espaço e seguido do valor, com 2 casas decimais, conforme o exemplo abaixo.
'''

N = int(input())
for n in range(N):
    feira = {}
    total = 0
    M = int(input())
    for m in range(M):
        entrada = str(input()).split()
        feira[entrada[0]] = float(entrada[1])
    P = int(input())
    for p in range(P):
        entrada_2 = str(input()).split()
        produto = entrada_2[0]
        qt = int(entrada_2[1])
        total += feira[produto] * qt
    print('R$ {:.2f}'.format(total))
        
