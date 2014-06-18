-- Code Golf
import Data.List

-- exer 1 
skips :: [a] -> [[a]]
skips l = map (everyNth l) [1..(length l)]

everyNth l n = case drop (n - 1) l of
               (x:xs) -> x : everyNth xs n
               [] -> []

-- exer 2
-- works because list comp. ignores failed pattern matches
localMaxima xs = [y | (x:y:z:_) <- tails xs, x < y && z < y]

-- exer 3
--histogram :: [Integer] -> String
histogram l = (hist . transpose . group $ sort l) ++ c
              where c = "\n==========\n0123456789\n"

-- stringifies list of lists repr. the rows of the histogram
hist l = intercalate "\n" $ reverse $ map stringify l 

-- converts a list of int to a string of whitespace and *
-- the ints in the list represent the indices of a 9-length blank string where
-- a * should be
--
-- replaceI replaces the char at index i with *
stringify l = 
          foldl replaceI s l 
          where s = replicate 10 ' '
                replaceI l n = a ++ ('*':b)
                             where (a, (_:b)) = splitAt n l

