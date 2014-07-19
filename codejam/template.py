import sys

def solve(

if __name__ == "__main__":
    args = sys.argv
    
    f = open(args[1], 'r')
    o = open(args[2], 'w')

    testcases = int(f.readline().strip())

    for t in xrange(1, testcases+1):
        (n, m, o) = map(int, f.readline().strip().split())
        l = f.readline().strip()
    
        res = solve(
        s = "Case #%d: %s\n" % (t, res)
        o.write(s)
