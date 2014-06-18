{-# LANGUAGE TypeSynonymInstances #-}
{-# LANGUAGE FlexibleInstances #-}

import ExprT
import Parser
--import StackVM -- for exer 5
import qualified Data.Map as M -- for exer 6
                                        
-- exer 1
eval :: ExprT -> Integer
eval (Lit x) = x
eval (Add a b) = (eval a) + (eval b)
eval (Mul a b) = (eval a) * (eval b)

-- exer 2
evalStr :: String -> Maybe Integer
evalStr = helper . parseExp Lit Add Mul 
        where helper Nothing = Nothing
              helper (Just e) = Just $ eval e

-- exer 3
class Expr a where
      lit ::  Integer -> a
      add :: a -> a -> a
      mul :: a -> a -> a

instance Expr ExprT where
         lit x = Lit x
         add a b = Add a b
         mul a b = Mul a b

-- exer 4
instance Expr Integer where
         lit x = x
         add a b = a + b
         mul a b = a * b

instance Expr Bool where
         lit x = x > 0
         add a b = a || b
         mul a b = a && b

newtype MinMax = MinMax Integer 
        deriving (Eq, Show)

instance Expr MinMax where
         lit x = MinMax x
         add (MinMax a) (MinMax b) = MinMax $ max a b
         mul (MinMax a) (MinMax b) = MinMax $ min a b

newtype Mod7 = Mod7 Integer 
        deriving (Eq, Show)

instance Expr Mod7 where
         lit x = Mod7 $ x `mod` 7
         add (Mod7 a) (Mod7 b) = Mod7 $ (a + b) `mod` 7
         mul (Mod7 a) (Mod7 b) = Mod7 $ (a * b) `mod` 7

testExp :: Expr a => Maybe a
testExp = parseExp lit add mul "(3 * -4) + 5"

-- exer 5
-- instance Expr Program where
--          lit x = [PushI x]
--          add x y = x ++ y ++ [Add]
--          mul x y = x ++ y ++ [Mul]

-- compile :: String -> Maybe Program
-- compile s = parseExp lit add mul 

-- exer 6
class HasVars a where
      var :: String -> a

data VarExprT = VarLit Integer
              | VarAdd VarExprT VarExprT
              | VarMul VarExprT VarExprT
              | Var String
              deriving Show

instance Expr VarExprT where
         lit x = VarLit x
         add x y = VarAdd x y
         mul x y = VarMul x y

instance HasVars VarExprT where
         var s = Var s


instance HasVars (M.Map String Integer -> Maybe Integer) where
         var s = M.lookup s

instance Expr (M.Map String Integer -> Maybe Integer) where
         lit x = (\_ -> Just x)
         add a b = 
        --  add (\_ -> Just a) (\_ -> Just b) = (\_ -> Just (a + b))

-- add (lit 2) (lit 3)