module Party where

import Employee
import Data.Monoid
import Data.Tree

glCons :: Employee -> GuestList -> GuestList
glCons e (GL l f) = GL (e:l) (empFun e + f)

instance Monoid GuestList where
         mempty = GL [] 0
         mappend (GL a c) (GL b d) = GL (a ++ b) (c + d)

moreFun :: GuestList -> GuestList -> GuestList
moreFun = max

treeFold :: (b -> a -> b) -> b -> Tree a -> b
treeFold f z (Node v ts) = foldl (treeFold f) (f z v) ts

nextLevel :: Employee -> [(GuestList, GuestList)] -> (GuestList, GuestList)
nextLevel gls boss = swap $ foldl combineAll base addBossToSnd
                   where combineAll (l,r) (a,b) = (l <> a, r <> b)
                         base = (GL [] 0,GL [] 0) 
                         addBossToSnd = map (\(l,r) -> (l, glCons boss r)) gls
                         swap (l,r) = (r,l)

--maxFun :: Tree Employee -> GuestList
maxFun tree = treeFold f base tree 

-- testing
boss = Emp "Sam" 10