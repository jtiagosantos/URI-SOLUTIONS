{-
Devita é o príncipe dos Calsadins. Juntamente com Pana, eles vão atrás de Tataroko, o nome de nascimento de Kogu, para tentar dominar o mundo. Ele possui um rastreador que mede o nível de energia de qualquer ser vivo. Todos os seres com o nível menor ou igual a 8000, ele considera como se fosse um inseto. Quando passa deste valor, que foi o caso de Kogu, ele se espanta e grita “Mais de 8000”. Baseado nisso, utilize a mesma tecnologia e analise o nível de energia dos seres vivos.

Entrada
A entrada é composta por vários casos de teste. A primeira linha contém um número inteiro C relativo ao número de casos de teste. Em seguida, haverá C linhas, com um número inteiro N (100 <= N <= 100000) relativo ao nível de energia de um ser vivo.

Saída
Para cada valor lido, imprima o texto correspondente.
-}

saida :: Int -> String
saida x | (x <= 8000) = "Inseto!"
        | otherwise = "Mais de 8000!"

loop 0 = return ()
loop n = do
  energia <- readLn :: IO Int
  let s = saida (energia)
  putStrLn (s)
  loop(n-1)

main = do
  n <- readLn :: IO Int
  loop (n)