{-
O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Coloque sete espaços em branco e coloque o carácter 'A';
Coloque seis espaços em branco e coloque o carácter 'B', um espaço em branco e o carácter 'B';
Coloque cinco espaços em branco e coloque o carácter 'C', três espaço em branco e o carácter 'C';
Coloque quatro espaços em branco e coloque o carácter 'D', cinco espaço em branco e o carácter 'D';
Coloque três espaços em branco e coloque o carácter 'E', sete espaço em branco e o carácter 'E';
Repita o procedimento 4;
Repita o procedimento 3;
Repita o procedimento 2;
Repita o procedimento 1.
Entrada
Não há.

Saída
O resultado de seu programa deve ser escrito conforme o exemplo de saída.
-}

import Text.Printf

main = do	
printf "       A\n"
printf "      B B\n"
printf "     C   C\n"
printf "    D     D\n"
printf "   E       E\n"
printf "    D     D\n"
printf "     C   C\n"
printf "      B B\n"
printf "       A\n"