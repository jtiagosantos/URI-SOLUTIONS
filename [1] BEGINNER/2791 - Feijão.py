'''
Conta-se nos arredores de Montes Claros que, há muito tempo no mercado municipal, Sebastião e seus companheiros de trabalho sempre jogam uma partida de adivinhação após a entrega dos produtos agrícolas colhidos na semana que se passou. O jogo, que se chama Adivinhe Onde o Feijão Está'', consiste em esconder um grão de feijão em um de quatro copos opacos e, depois de embaralhá-los, o apostador deve adivinhar em qual copo o legume está.

https://resources.urionlinejudge.com.br/gallery/images/contests/feijao.png

Neste ano, devido ao grande sucesso cultural e histórico e à enorme quantidade de pessoas que praticam este jogo no mercado municipal, a prefeitura resolveu realizar um campeonato de Adivinhe Onde o Feijão Está''. Entretanto, ela necessita de um programa para mostrar aos expectadores onde o feijão estava após o fim de uma partida. Sabendo que a próxima Maratona Mineira de Programação ocorrerá na cidade, ela logo encomendou uma solução aos exímios programadores. Desta forma, você deve auxiliar a organização nesta missão com um programa que informe, ao fim de uma partida, onde o feijão esteve.

Entrada
A entrada conterá apenas uma linha com quatro inteiros, C1, C2, C3 e C4 separados por um espaço. O valor Ci=1 indica que o feijão estava no copo número i, e Ci=0 indica que o i-ésimo copo estava vazio ao fim da partida. Haverá sempre exatamente um copo com o feijão.

Saída
Escreva na saída uma linha contendo um inteiro entre 1 e 4, correspondendo à posição onde o feijão estava.
'''

valores = str(input()).split()
for k, v in enumerate(valores):
    valores[k] = int(v)
print(valores.index(1)+1)
