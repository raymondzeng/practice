module JoinList where

import Data.Monoid
import Sized
import Scrabble

data JoinList m a = Empty
                  | Single m a
                  | Append m (JoinList m a) (JoinList m a)
                  deriving (Eq, Show)

(+++) :: Monoid m => JoinList m a -> JoinList m a -> JoinList m a
(+++) l r = Append ((annot l) `mappend` (annot r)) l r
      where annot Empty = mempty
            annot (Single m _) = m
            annot (Append m _ _) = m

tag :: Monoid m => JoinList m a -> m
tag Empty = mempty
tag (Single m _) = m
tag (Append m _ _) = m

indexJ :: (Sized b, Monoid b) => Int -> JoinList b a -> Maybe a
indexJ i Empty = Nothing
indexJ i (Single _ a) 
       | i /= 0 = Nothing
       | otherwise = Just a
indexJ i (Append m l r) 
       | i < 0 = Nothing
       | i > sm = Nothing
       | i < sl = indexJ i l
       | i >= sl = indexJ (i - sl) r
       where sm = getSize $ size m
             sl = getSize . size $ tag l
             getSize (Size s) = s
                          

(!!?) :: [a] -> Int -> Maybe a
[] !!? _ = Nothing
_ !!? i | i < 0 = Nothing
(x:xs) !!? 0 = Just x
(x:xs) !!? i = xs !!? (i-1)

jlToList :: JoinList m a -> [a]
jlToList Empty = []
jlToList (Single _ a) = [a]
jlToList (Append _ l1 l2) = jlToList l1 ++ jlToList l2

-- should add check for negative int
dropJ :: (Sized b, Monoid b) => Int -> JoinList b a -> JoinList b a
dropJ i a | i <= 0 = a
dropJ _ (Single _ _) = Empty
dropJ i (Append m l r) 
      | i >= sm = Empty
      | i >= sl = (dropJ (i - sl) r)
      | otherwise = (dropJ i l) +++ r
      where sm = getSize $ size m
            sl = getSize . size $ tag l

takeJ :: (Sized b, Monoid b) => Int -> JoinList b a -> JoinList b a
takeJ i _ | i <=0 = Empty
takeJ i j@(Single _ _) = j
takeJ i j@(Append m l r) 
      | i >= sm = j
      | i <= sl = (takeJ i l)
      | otherwise = (takeJ i l) +++ (takeJ (i - sl) r)
      where sm = getSize $ size m
            sl = getSize . size $ tag l


scoreLine :: String -> JoinList (Score, Size) String
scoreLine s = Single (scoreString s, Size 1) s