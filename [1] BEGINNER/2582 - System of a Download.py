'''
System of a Download é uma famosa banda de Hacker Metal! Certa vez, eles criaram um dispositivo, com seis botões, numerados de 0 a 5, e colocaram nesse dispositivo os seus 11 maiores sucessos. Para tocar uma destas músicas, é preciso pressionar dois botões. Com isso, os números destes dois botões são somados, e então toca-se a música correspondente ao número da soma, conforme a relação abaixo:

0 - PROXYCITY
1 - P.Y.N.G.
2 - DNSUEY!
3 - SERVERS
4 - HOST!
5 - CRIPTONIZE
6 - OFFLINE DAY
7 - SALT
8 - ANSWER!
9 - RAR?
10 - WIFI ANTENNAS


Por exemplo, se os botões pressionados forem 3 e 4, irá tocar a música 7 - SALT
Escreva um programa que, dados os dois botões que forem pressionados, determine qual música irá tocar.

Entrada
Um número inteiro C será informado, que será a quantidade de casos de teste. Cada caso tem dois valores inteiros, X e Y, representando quais botões foram pressionados.

Saída
Para cada caso de teste, imprima o nome da música correspondente.
'''

musicas = {
    '0':'PROXYCITY',
    '1':'P.Y.N.G.',
    '2':'DNSUEY!',
    '3':'SERVERS',
    '4':'HOST!',
    '5':'CRIPTONIZE',
    '6':'OFFLINE DAY',
    '7':'SALT',
    '8':'ANSWER!',
    '9':'RAR?',
    '10':'WIFI ANTENNAS'
}

C = int(input())
for i in range(C):
    entrada = str(input()).split()
    for k,v in enumerate(entrada):
        entrada[k] = int(v)
    soma = sum(entrada)
    soma = str(soma)
    print(musicas[soma])

