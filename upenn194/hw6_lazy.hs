data Stream a = Cons a (Stream a)

instance Show a => Show (Stream a) where
         show s = show $ take 20 $ streamToList s

streamToList :: Stream a -> [a]
streamToList (Cons a as) = a : streamToList as

streamRepeat :: a -> Stream a
streamRepeat e = es
             where es = Cons e es

streamMap :: (a -> b) -> Stream a -> Stream b
streamMap f (Cons x xs) = Cons (f x) $ streamMap f xs

streamFromSeed :: (a -> a) -> a -> Stream a
streamFromSeed f e = Cons e $ streamFromSeed f (f e)


nats :: Stream Integer
nats = streamFromSeed (+1) 0

ruler :: Stream Integer
ruler = streamMap pow2 $ streamFromSeed (+1) 1 

pow2 :: Integer -> Integer
pow2 x
     | x `mod` 2 == 0 = 1 + (pow2 $ x `div` 2)
     | otherwise = 0


-- fibs
-- exer 6 and 7
