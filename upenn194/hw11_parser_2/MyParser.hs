import           AParser
import           Control.Applicative
import           Data.Char

sequenceA :: (Applicative f) => [f a] -> f [a]  
sequenceA = foldr (liftA2 (:)) (pure [])  

zeroOrMore :: Parser a -> Parser [a]
zeroOrMore p = sequenceA [p,p,p] 

matchOne :: Parser a -> Parser [a]
matchOne p = (\x -> [x]) <$> p

oneOrMore :: Parser a -> Parser [a]
oneOrMore p = (\as bs -> as ++ bs) <$> (matchOne p) <*> (zeroOrMore p)