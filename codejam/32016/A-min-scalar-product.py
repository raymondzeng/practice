import sys

def solve(v1, v2):
    v1.sort()
    v2.sort()
    v2 = reversed(v2)
    
    return sum([a * b for (a,b) in zip(v1, v2)])

if __name__ == "__main__":
    args = sys.argv
    
    f = open(args[1], 'r')
    o = open(args[2], 'w')

    testcases = int(f.readline().strip())

    for t in xrange(1, testcases+1):
        _ = f.readline()
        v1 = map(int, f.readline().strip().split())
        v2 = map(int, f.readline().strip().split())
    
        res = solve(v1, v2)

        s = "Case #%d: %i\n" % (t, res)
        o.write(s)
