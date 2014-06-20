import AParser
import Data.
zeroOrMore :: Parser a -> Parser [a]
zeroOrMore p = listWrap <$> p
             where listWrap x = [x]