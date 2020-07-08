'''
Amarelinha provavelmente é a brincadeira em que as crianças da vila mais se divertem, porém a mesma vem causando um bom tempo de discussão e choro nas crianças que a praticam. A causa do transtorno é para decidir quem será o próximo a pular, mas recentemente Quico (O gênio!) teve uma grande ideia para solucionar o problema. Basicamente a brincadeira só poderá ser jogada de dois em dois jogadores e para escolher o próximo jogador Quico indicou o uso do tradicional método par ou ímpar, onde os dois jogadores informam um número e se a soma desses números for par o jogador que escolheu PAR ganha ou vice verso. Entretanto a utilização desse método vem deixando o Quico louco, louco, louco... E por esse motivo ele pediu a sua ajuda! Solicitou a você um programa que dado o nome dos jogadores, suas respectivas escolhas PAR ou IMPAR e os números, informe quem foi o vencedor.

Entrada
A primeira linha de entrada contém um número inteiro QT (1 ≤ QT ≤ 100), indicando a quantidade de casos de teste que vem a seguir. Cada caso de teste contém duas linhas. Na primeira linha será informado o nome do jogador 1 seguido de sua escolha, “PAR” ou “IMPAR” e logo após, o nome do jogador 2 seguido de sua escolha, “PAR” ou “IMPAR”. Na segunda linha de entrada, contém 2 números inteiros N (1 ≤ N ≤ 10⁹) e M (1 ≤ M ≤ 10⁹), representando respectivamente os números escolhidos pelo jogador 1 e pelo jogador 2. É garantido que a escolha (PAR ou IMPAR) do jogador 1 será diferente da escolha (PAR ou IMPAR) do jogador 2 e que o nome dos jogares são formados somente por letras e não ultrapassarão 100 caracteres.

Saída
Para cada caso de teste, imprima uma única linha contendo o nome do jogador vencedor.
'''

QT = int(input())
for i in range(QT):
    entrada_1 = str(input()).split()
    j1 = entrada_1[0]
    tipo_j1 = entrada_1[1]
    j2 = entrada_1[2]
    tipo_j2 = entrada_1[3]
    entrada_2 = str(input()).split()
    v1 = int(entrada_2[0])
    v2 = int(entrada_2[1])
    soma = v1 + v2
    if soma % 2 == 0:
        if tipo_j1 == 'PAR':
            print(j1)
        if tipo_j2 == 'PAR':
            print(j2)
    if soma % 2 != 0:
        if tipo_j1 == 'IMPAR':
            print(j1)
        if tipo_j2 == 'IMPAR':
            print(j2)
