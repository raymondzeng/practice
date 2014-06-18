-- | Ans: 906609
import qualified Data.List

toDigits n 
         | n <= 0 = []
         | otherwise = toDigits (n `div` 10) ++ [n `mod` 10]

isPalDigits d 
             | null d = True
             | even $ length d = 
                             let secondHalf = reverse $ snd $ splitAt indx d
                             in firstHalf == secondHalf
             | otherwise =
                         let secondHalf = reverse $ tail $ snd $ splitAt indx d
                         in firstHalf == secondHalf
             where indx = length d `div` 2
                   firstHalf = fst $ splitAt indx d

isPal n = isPalDigits $ toDigits n

-- much simpler
isPal' n = show n == (reverse $ show n)

largestPal3x3 = Data.List.find isPal' $ reverse . Data.List.sort $ allProducts range
    where range = [999, 998..100]
          allProducts [] = []
          allProducts l@(x:xs) = allProducts xs ++ map (* x) l
