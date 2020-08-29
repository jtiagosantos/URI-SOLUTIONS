'''
As sequências de Iccanobif são sequências onde cada termo é sempre igual a soma dos dois próximos subsequentes a eles.
Exceto pelos dois últimos termos os quais são sempre iguais a 1.

Exemplo de uma sequência de Iccanobif com 10 termos: 55, 34, 21, 13, 8, 5, 3, 2, 1, 1.

Sua tarefa é, dado um valor inteiro, imprimir a sequência de Iccanobif de tamanho correspondente.

Entrada
A entrada consiste de um único inteiro N (1 ≤ N ≤ 40) representando o tamanho da sequência de Iccanobif desejada.

Saída
A saída consiste de um única linha contendo os termos da sequência de Iccanobif de tamanho N separados por um único 
espaço em branco.
'''

N = int(input()); sequencia = []

t1, t2, t3, i = 1, 1, 0, 0; 

if N >= 2:
    sequencia.append(t1); sequencia.append(t2)
else:
    sequencia.append(1)

for _ in range(N-2):
    t3 = t1 + t2
    sequencia.append(t3)
    t1 = t2
    t2 = t3
    
print('{}'.format(' '.join([str(i) for i in sequencia][::-1])))