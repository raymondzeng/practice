import sys
import math

def solve(n):
    s = 3 + math.sqrt(5)
    s = s ** n
    ans = str(int(math.floor(s) % 1000))
    
    to_pad = 3 - len(ans)
    if to_pad != 0:
        padding = "0" * to_pad
        ans = padding + ans

    return ans

    
if __name__ == "__main__":
    args = sys.argv
    
    f = open(args[1], 'r')
    o = open(args[2], 'w')

    testcases = int(f.readline().strip())

    for t in xrange(1, testcases+1):
        n = int(f.readline().strip())
        
        res = solve(n)
        s = "Case #%d: %s\n" % (t, res)
        o.write(s)
