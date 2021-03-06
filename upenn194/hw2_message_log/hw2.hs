import Log

-- exer 1
readMaybe s = case reads s of
       [(a, "")] -> Just a
       _ -> Nothing 

parseMessage :: String -> LogMessage
parseMessage s = parseHelper $ words s

parseHelper l@("E":a:b:xs)
                | aMaybe == Nothing = Unknown $ unwords l
                | bMaybe == Nothing = Unknown $ unwords l
                | otherwise = messageBuilder (errorJust aMaybe) bMaybe xs
                where aMaybe = readMaybe a :: Maybe Int
                      bMaybe = readMaybe b :: Maybe Int
parseHelper l@(a:b:xs)
               | bMaybe == Nothing = Unknown $ unwords l
               | a == "I" = messageBuilder Info bMaybe xs
               | a == "W" = messageBuilder Warning bMaybe xs
               where bMaybe = readMaybe b :: Maybe Int

errorJust (Just a) = Error a
messageBuilder a (Just b) xs = LogMessage a b $ unwords xs

parse :: String -> [LogMessage]
parse s = map parseMessage $ lines s

-- exer 2
-- assumes timestamps are unique
insert :: LogMessage -> MessageTree -> MessageTree
insert (Unknown _) t = t
insert l@(LogMessage _ n _) Leaf = Node Leaf l Leaf
insert l@(LogMessage _ n _) (Node left lm@(LogMessage _ time _) right) 
       | n < time = Node (insert l left) lm right
       | n > time = Node left lm (insert l right)
       | otherwise = error "timestamps must be unique"
       
-- exer 3
build :: [LogMessage] -> MessageTree
build l = foldr insert Leaf l

-- exer 4
inOrder :: MessageTree -> [LogMessage]
inOrder Leaf = []
inOrder (Node left m right) =
        inOrder left ++ [m] ++ inOrder right

-- exer 5
whatWentWrong :: [LogMessage] -> [String]
whatWentWrong xs = map extractString $ sort $ filter isRelevant xs
              where extractString (LogMessage _ _ m) = m
                    sort = inOrder . build 
                    isRelevant (LogMessage (Error n) _ _) = n > 50
                    isRelevant _ = False