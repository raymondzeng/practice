import Data.List 

f n = logs 
      where logs = length . takeWhile (>= 0) $ unfoldr logCycle n
            logCycle x = Just (a, x') 
                         where a = fromIntegral . floor $ logBase 2 x
                               x' = x - (2 ** a)