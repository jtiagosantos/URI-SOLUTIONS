'''
Como se sabe, léxico é o conjunto de palavras que existe em uma língua. Nas línguas ocidentais, é comum escrever usando o 
alfabeto latino, com 26 letras que vão de a até z.
É comum enumerar as letras na seguinte ordem: a, b, c, d, e f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z.
Se uma lista de palavras está organizadas de acordo com esta ordem, fica muito mais rápido pesquisá-las. 
Seu trabalho neste problema é ordenar duas palavras de acordo com esta ordem.

Sejam duas palavras A e B. Caso o primeiro caractere de A venha antes do primeiro de B, coloca-se A antes de B. 
Se o primeiro caractere for igual, usa-se o seguinte para desempate. E se o segundo empatar, usa-se o terceiro, etc. 
Quando todos os caracteres de A forem iguais ao começo de B, ou todos os de B forem iguais ao começo de A, coloca-se a 
menor palavra primeiro.

Entrada
A entrada contém 2 palavras com caracteres minúsculos de a até z, O comprimento das palavras não ultrapassa 20 caracteres.

Saída
A saída contém as mesmas 2 palavras, só que na ordem lexicográfica.
'''

words = []; words.append(str(input())); words.append(str(input())); words = sorted(words); print(words[0]); print(words[1])