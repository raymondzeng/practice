def reverseWords(s):
    s = s.strip()
    words = s.split()
    
    flipped = flipAll(words)
        
    return " ".join(flipped)
    
def flipAll(l):
    start = 0
    end = len(l) - 1
        
    while (start < end):
        print end
        temp = l[end]
        l[end] = l[start]
        l[start] = temp
        start += 1
        end -= 1
            
    return l 

print reverseWords("hello there sky")
