'''
Bino e Cino são colegas inseparáveis. Bino gosta de criar desafios matemáticos para Cino resolver. Desta vez, Bino gerou uma lista de números e perguntou ao Cino quantos números da lista são múltiplos de 2, 3, 4 e 5.

Esse desafio pode parecer simples, porém, quando a lista contém muitos números, Cino se confunde e acaba errando alguns cálculos. Para ajudar Cino, faça um programa para resolver o desafio de Bino.

Entrada
A primeira linha da entrada consiste em um inteiro N (1 ≤ N ≤1000), representando a quantidade de números na lista de Bino.

A segunda linha contém N inteiros Li (1 ≤ Li ≤ 100), representando os números da lista de Bino.

Saída
Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista. Observe a formatação da saída nos exemplos, pois ela deve ser seguida rigorosamente.
'''

N = int(input())
entrada = str(input()).split()
for k, v in enumerate(entrada):
    entrada[k] = int(v)
m_dois = m_tres = m_quatro = m_cinco = 0
for i in entrada:
    if i % 2 == 0:
        m_dois += 1
    if i % 3 == 0:
        m_tres += 1
    if i % 4 == 0:
        m_quatro += 1
    if i % 5 == 0:
        m_cinco += 1
print('{} Multiplo(s) de 2'.format(m_dois))
print('{} Multiplo(s) de 3'.format(m_tres))
print('{} Multiplo(s) de 4'.format(m_quatro))
print('{} Multiplo(s) de 5'.format(m_cinco))
