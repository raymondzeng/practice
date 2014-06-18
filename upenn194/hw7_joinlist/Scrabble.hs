{-# LANGUAGE GeneralizedNewtypeDeriving, FlexibleInstances #-}
module Scrabble where

import Data.Monoid

newtype Score = Score Int
  deriving (Eq, Ord, Show, Num)

getScore :: Score -> Int
getScore (Score i) = i

getScore' :: (Score, t) -> Int
getScore' (Score i, _) = i

instance Monoid Score where
  mempty  = Score 0
  mappend = (+)

score :: Char -> Score
score c = case c of
          'a' -> Score 1
          'b' -> Score 3
          'c' -> Score 3
          'd' -> Score 2
          'e' -> Score 1
          'f' -> Score 4
          'z' -> Score 10
          _ -> mempty

scoreString :: String -> Score
scoreString = mconcat . map score 