-- | Ans: 4613732
import Data.List 

-- _lots_ of repeated calculations
sumEvenFibs lim = 
            let fib 1 = 1
                fib 2 = 2
                fib n = fib (n - 1) + fib (n - 2)
            in sum [x | x <- takeWhile (< lim) $ map fib [1..], even x]

-- no repeated calculations
sumEvenFibs' lim = 
             sum [x | x <- takeWhile (< lim) $ fiblist (1,2), 
                                  even x]
             where fiblist = unfoldr (\(a, b) -> Just (a, (b, a + b)))    
