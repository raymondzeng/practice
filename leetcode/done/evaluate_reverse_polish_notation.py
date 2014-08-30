# @param tokens, a list of string
# @return an integer
import math

def evalRPN(tokens):
    stack = []
    for t in tokens:
        try:
            stack.append(int(t))
        except:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(int(float(a) / float(b)))
            else:
                print "Unknown " + t
        print stack
    return stack.pop()


print evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print evalRPN(["4", "13", "5" , "/" , "+"])
