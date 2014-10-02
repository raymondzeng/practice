def matches(s):
    match = {"(": ")",
             "[": "]",
             "{": "}" }
    stack = []
    
    for c in s:
        if not stack:
            stack.append(c)
        elif match[stack[-1]] == c:
            stack.pop()
        elif c not in match:
            return False
        else:
            stack.append(c)

    return len(stack) == 0

print matches("()")
print matches("(())")
print matches("({}{})")
print matches("")
print matches(")(") # broken

        
            
