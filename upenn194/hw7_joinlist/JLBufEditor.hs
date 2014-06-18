module Main where

import JLBuffer
import Editor
import JoinList
import Scrabble
import Sized

main = runEditor editor $ Single (Score 10, Size 1) "z" +++ (Single (Score 1, Size 1) "a")