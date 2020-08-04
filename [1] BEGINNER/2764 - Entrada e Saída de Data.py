'''
O seu professor gostaria de fazer um programa com as seguintes características:

    1.Leia uma data no formato DD/MM/AA;
    2.Imprima a data no formato MM/DD/AA;
    3.Imprima a data no formato AA/MM/DD;
    4.Imprima a data no formato DD-MM-AA.

Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha tem o seguinte formato DD/MM/AA onde DD, MM, AA são números inteiros. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas conforme os procedimentos 2, 3 e 4. Conforme mostra o exemplo de saída a seguir.
'''

data = str(input()).split(sep='/')

dia = data[0]
mes = data[1]
ano = data[2]

print('{}/{}/{}'.format(mes, dia, ano))
print('{}/{}/{}'.format(ano, mes, dia))
print('{}-{}-{}'.format(dia, mes, ano))
