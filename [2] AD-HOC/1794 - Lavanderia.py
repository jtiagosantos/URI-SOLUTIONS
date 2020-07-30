'''
Cansada de lavar suas roupas sujas, sua mãe decidiu que a partir de agora quem lava suas roupas é você.

Na lavanderia da sua casa existe uma lavadora e uma secadora de roupas, cada uma com um limite mínimo e máximo de peças a serem lavadas e secadas por vez. Assim sendo, a lavadora só deve ser usada se forem colocadas no mínimo LA e no máximo LB peças dentro dela, e semelhantemente a secadora só deve ser usada se forem colocadas no mínimo SA e no máximo SB peças dentro dela.

Você tem atualmente N peças de roupa a serem lavadas e secadas, e quer descobrir se é possível usar a lavadora e secadora para lavar e secar todas as suas peças, seguindo as regras acima.

Entrada
Na primeira linha da entrada haverá um inteiro N (1 ≤ N ≤ 100).

Na segunda linha da entrada haverá dois inteiros LA e LB (1 ≤ LA < LB ≤ 100).

Na terceira linha da entrada haverá dois inteiros SA e SB (1 ≤ SA < SB ≤ 100).

Saída
Imprima a palavra "possivel" caso seja possível lavar e secar suas peças de roupa seguindo as regras descritas no enunciado, ou "impossivel" caso contrário.
'''

num_roupas = int(input())
entrada_1 = str(input()).split()
La, Lb = int(entrada_1[0]), int(entrada_1[1])
entrada_2 = str(input()).split()
Sa, Sb = int(entrada_2[0]), int(entrada_2[1])
if La <= num_roupas <= Lb and Sa <= num_roupas <= Sb:
    print('possivel')
else:
    print('impossivel')