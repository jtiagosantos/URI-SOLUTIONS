{-
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.
-}

tamanho_lista :: [Int] -> String
tamanho_lista lista | (length (lista) == 2) = " eh primo"
                    | otherwise = " nao eh primo"

loop 0 = return ()
loop n = do
  num <- readLn :: IO Int
  let lista = [i | i <- [1..num], mod num i == 0]
  let saida = tamanho_lista (lista)
  putStr (show(num))
  putStrLn saida
  loop (n-1)

main = do
  n <- readLn :: IO Int
  loop n