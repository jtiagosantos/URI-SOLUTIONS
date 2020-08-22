'''
O governo da Taxilândia está enfrentando um enorme problema, os taxilandenses amam carros e velocidade, por isso estão correndo muito nas avenidas da cidade. Para amenizar esse problema o governo vai instalar radares nas avenidas, de modo que cada trecho seja coberto por pelo menos um radar. É importante saber que um radar cobre M quilômetros contíguos da avenida.

Você foi contratado pelo governo para fazer um programa que dado o comprimento da avenida e a área de cobertura do radar, informe a quantidade mínima de radares necessários para cobrir a avenida.

A imagem abaixo mostra uma avenida de tamanho 15 quilômetros e radares com cobertura de 4 quilômetros, cada cor representa um radar, então é possível notar que a quantidade mínima de radares necessários para cobrir a avenida é 4.

https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2598.png

Entrada
A primeira linha consiste em um inteiro C que representa a quantidade de casos de teste. Cada caso de teste é composto por dois inteiros N e M que indicam o tamanho da avenida e a área de cobertura do radar.

(1 ≤ N ≤ 109)

(1 ≤ M ≤ 109)

Saída
Seu programa deve exibir a menor quantidade de radares necessários para cobrir toda avenida.
'''

C = int(input())
for _ in range(C):
    entrada = str(input()).split()
    N = int(entrada[0])
    M = int(entrada[1])
    count = i = 0
    while i < N:
        i += M
        count += 1
    print(count)

