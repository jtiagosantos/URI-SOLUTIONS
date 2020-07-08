'''
Gilberto é um famoso vendedor de esfirras na região. Porém, apesar de todos gostarem de suas esfirras, ele só sabe dar o troco com duas notas, ou seja, nem sempre é possível receber o troco certo. Para facilitar a vida de Gil, escreva um programa para ele que determine se é possível ou não devolver o troco exato utilizando duas notas.

As notas disponíveis são: 2, 5, 10, 20, 50 e 100.

Entrada
A entrada deve conter o valor inteiro N da compra realizada pelo cliente e, em seguida, o valor inteiro M pago pelo cliente (N < M ≤ 104). A entrada termina com N = M = 0.

Saída
Seu programa deverá imprimir "possible" se for possível devolver o troco exato ou "impossible" se não for possível.
'''

notas = [2, 5, 10, 20, 50, 100]

while True:
    entrada = str(input()).split()
    N = int(entrada[0])
    M = int(entrada[1])
    if N == M == 0:
        break
    troco = M - N
    soma = 0
    for c in notas:
        for i in notas:
            if c + i == troco:
                soma += 1
    if soma == 2:
        print('possible')
    else:
        print('impossible')
        