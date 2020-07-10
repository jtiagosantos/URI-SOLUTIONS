'''
Frodo e Sam estão prestes a conseguir jogar o anel na Montanha da Perdição, porém Gollum os atrapalha.
Uma pequena pausa na história. Senhor dos Anéis, além de ser um dos maiores clássicos literários e cinematográficos da humanidade, é uma história que deixa evidente o valor da amizade. Dê valor às boas amizades :) Despause.
Gollum é um ser infeliz e que não suporta a amizade. Para que Frodo e Sam consigam passar por ele, eles precisam recitar runas que entoam amizade. Cada runa é representada por uma letra do alfabeto, e indica uma quantidade de amizade que ela emite, podendo ser positiva ou negativa (sim, existem as runas que representam as más amizades). 
Dada a quantidade de amizade necessária para derrotar Gollum, uma lista de runas e seus respectivos valores de amizade e as runas que Sam e Frodo recitaram, dê o valor final de amizade que Frodo e Sam conseguiram e se foi possível ou não derrotar Gollum.

Entrada
A primeira linha da entrada é composta por dois inteiros N(1 <= N) e G(G <= 100), indicando, respectivamente, a quantidade de runas existentes, e a quantidade de amizade necessária para derrotar Gollum. As próximas N linhas são compostas por um caractere Ri('A' <= Ri <= 'Z') e um inteiro Vi(-100 <= Vi <= 100), indicando, respectivamente, a runa e o valor de amizade que ela agrega. A próxima linha é iniciada por um inteiro X, indicando a quantidade de runas recitadas por Frodo e Sam. A última linha da entrada é composta por X caracteres, indicando as runas recitadas por Frodo e Sam.

Saída
A primeira linha da saída deve conter a quantidade de valor de amizade. A segunda linha deve conter uma das seguintes mensagens:
● “My precioooous”, se Gollum vencer;
● “You shall pass!”, se Frodo e Sam vencerem.
'''

entrada_1 = str(input()).split()
N = int(entrada_1[0])
G = int(entrada_1[1])

letras = []
valores = []
for i in range(N):
    entrada_2 = str(input()).split()
    Ri = entrada_2[0].upper()
    Vi = int(entrada_2[1])
    letras.append(Ri)
    valores.append(Vi)
    
X = int(input())
entrada_3 = str(input()).split()

total_amizade = 0

for i in entrada_3:
    if i in letras:
        total_amizade += valores[letras.index(i)]

print(total_amizade)
if total_amizade >= G:
    print('You shall pass!')
else:
    print('My precioooous')
    