-- Exercise 1
toDigits :: Integer -> [Integer]
toDigits n 
         | n <= 0       = []
         | otherwise    = toDigits (n `div` 10) ++ [n `mod` 10]
         
toDigitsRev :: Integer -> [Integer]
toDigitsRev n 
            | n <= 0    = []
            | otherwise = [n `mod` 10] ++ toDigitsRev (n `div` 10)           

-- exercise 2
doubleEveryOther :: [Integer] -> [Integer]
doubleEveryOther l 
                 | null l = []
                 | null (tail l) = []
                 | otherwise = doubleEveryOther (init (init l)) 
                                  ++ [last (init l) * 2] 
                                  ++ [last l]

-- exer 3
-- will not work correctly if contains n-digit numbers where n > 2
sumDigits :: [Integer] -> Integer
sumDigits l = 
          sum [if x > 10 then (x `div` 10 + x `mod` 10) else x | x <- l]

-- exer 4
validate :: Integer -> Bool
validate n = 
         (sumDigits (doubleEveryOther (toDigits n)))
         `mod` 10 == 0

-- exer 5
type Peg = String
type Move = (Peg, Peg)
hanoi :: Integer -> Peg -> Peg -> Peg -> [Move]
hanoi 1 a b _ = [(a, b)]
hanoi n a b c = 
      (hanoi (n - 1) a c b) ++ [(a,b)] ++ (hanoi (n - 1) c b a)