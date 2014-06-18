-- | Ans: 232792560
import qualified Data.List

-- never tested with [1..20]. works with [1..10]
smallestDivByAll l = 
                 Data.List.find (\x -> divAll x l) [1..]
                 where divAll n l
                                 | null l = True
                                 | otherwise = n `mod` (head l) == 0 && 
                                               divAll n (tail l)

-- derp
answer = foldr lcm 1 [1..20]