{-# LANGUAGE FlexibleInstances, TypeSynonymInstances #-}
module JLBuffer where

import Data.Monoid
import Buffer
import JoinList
import Scrabble
import Sized

instance Buffer (JoinList (Score, Size) String) where
  toString     = unwords . jlToList 
  fromString   = scoreLine 
  line n b     = indexJ n b
  replaceLine n l b = takeJ n b +++ scoreLine l -- incomplete
  numLines     = getSize' . tag
  value        = getScore' . tag 
