'''
Uma formiguinha está andando sobre um tronco de árvore de tamanho N metros. Podemos considerar que a formiga pode assumir as posições de 0 até N-1. Assuma que ela está no eixo X dos planos coordenados, porém ela começa em uma posição desconhecida. A única coisa que se sabe sobre sua posição inicial é que é um número inteiro.

A formiguinha pode dar um passo para a esquerda ou direita, e este passo a desloca de um metro. Se ela está na posição P e dá um passo para a direita, ela assumirá a posição P+1. Se o passo for para a esquerda, ela assumirá a posição P-1. Se em algum momento ela assumir a posição -1 ou a posição N, ela cairá do tronco! Um passo leva um segundo para ser completado, e a formiga sempre está se movendo.

Considerando que a formiga fará sempre a pior sequência de passos possível, escolha uma posição inicial de modo que maximize o tempo em que a formiga permaneça no tronco. Imprima este tempo.

Entrada
Na primeira linha você terá um inteiro T (T <= 100) indicando o número de casos de teste.

Para cada caso teremos uma única linha com o número inteiro N (1 ≤ N ≤ 109) indicando o tamanho do tronco da árvore.

Saída
Para cada caso, imprima o tempo máximo que a formiguinha pode ficar no tronco.
'''

from math import ceil
T = int(input())
for t in range(T):
    tamanho = int(input())
    print(ceil(tamanho/2))