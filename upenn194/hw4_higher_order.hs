-- exer 1
fun1 :: [Integer] -> Integer
fun1 [] = 1
fun1 (x:xs)
     | even x = (x - 2) * fun1 xs
     | otherwise = fun1 xs

fun1' :: [Integer] -> Integer
fun1' = foldl (*) 1 . map (subtract 2) . filter even

fun2 :: Integer -> Integer
fun2 1 = 0
fun2 n | even n = n + fun2 (n `div` 2)
       | otherwise = fun2 (3 * n + 1)

fun2' x = sum . filter even . takeWhile (/= 1) $ iterate (\n -> if even n
                                                then n `div` 2
                                                else 3 * n + 1) x

-- exer 2
data Tree a = Leaf
            | Node Integer (Tree a) a (Tree a)
     deriving (Show, Eq)

foldTree :: [a] -> Tree a
foldTree = foldr insert Leaf
    
-- 95% it's correct (reading trees as strings is hard)
insert n Leaf = Node 0 Leaf n Leaf
insert n (Node h l v r) 
       | lh > rh = Node h l v (insert n r)
       | lh < rh = Node h nl v r
       | otherwise = Node (height nl) nl v r
       where nl = insert n l
             lh = height l
             rh = height r
             height Leaf = 0
             height (Node h _ _ _) = h + 1

-- exer 3
xor :: [Bool] -> Bool
xor l = odd $ foldl countTrue 0 l
        where countTrue acc x = if x then acc + 1 else acc

map' :: (a -> b) -> [a] -> [b]
map' f = foldr (\x acc -> (f x) : acc) [] 

-- exer 4
-- not very efficient/fast
--cartProd :: [a] -> [b] -> [(a, b)]
--cartProd xs ys = [(x,y) | x <- xs, y <- ys]

toDelete n = [i + j + 2 * i * j | i <- [1..n], j <- [i..n]]

-- doesn't use func comp like assgn says
sieveSundaram :: Integer -> [Integer]
sieveSundaram n = [x * 2 + 1 | x <- [1..(2 * n + 2)], not $ x `elem` bad]
                  where bad = toDelete n