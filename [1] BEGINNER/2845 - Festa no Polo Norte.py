'''
Giovana ficou muito feliz por conseguir mandar sua carta para o papai Noel e receber ótimos presentes. 
A alegria foi tanta que ela resolveu até convidar todos os duendes do bom velhinho para sua festa de aniversário, 
que é pouco depois do Natal, em Janeiro. Porém, ela não quer que o Grinch apareça na sua festinha para estragar tudo, 
então ela bolou um plano.

Para esconder do malvado Grinch onde será a festa, ela resolveu ultilizar o sistema de reuniões dos Duendes, que 
funciona assim: cada duende tem um identificador numérico único e, quando haverá uma reunião, é escolhida a casa de 
um dos duendes para sediar o encontro. Mas ao invés de escrever o número do duende anfitrião no mural da fábrica 
do Papai Noel, onde todos podem ver, é escrito o identificador de exatamente todos os duendes com números menores 
que o dele e que são coprimos ao dele. Esse método é também uma forma de dizer que esses duendes do mural devem 
levar as comidas e bebidas para a reunião.

Como o Grinch é tão ruim com números a ponto de nem saber que dois números só são chamados de coprimos se o MDC 
(máximo divisor comum) entre eles é 1, Giovana simplesmente envia uma carta para o polo norte com os números dos 
duendes que devem levar as comidas, e com isso, os duendes já conseguem descobrir onde será a festa de aniversário, 
mas o Grinch não.

Dada a carta que os duendes receberam, determine na casa de qual Duende será a festa de aniversário de Giovana.

Entrada
A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 104) o qual representa a quantidade de números escritos na carta de Giovana. A segunda linha da entrada possui N números inteiros Ai (1 ≤ Ai ≤ 105) representando os identificadores dos duendes escritos na carta.

Saída
A saída consiste de uma única linha contendo o número do duende que sediará a festa de Giovana em sua casa.
'''

N = int(input()); identificadores = str(input()).split()
identificadores = [int(i) for i in identificadores]
print(max(identificadores) + 1)