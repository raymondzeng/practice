import sys

def solve(credit, prices):
    """
    Since there is only one solution, iterate through list and check that element with every other elem in the list after that elem until you get the right sum.
    
    j is always guaranteed to be >= i
    Runtime = n^2
    """

    for i, price in enumerate(prices):
        for j, snd_price in enumerate(prices[i + 1:]):
            if price + snd_price == credit:
                return (i + 1, j + i + 2)

    return (-1, -1)

if __name__ == "__main__":
    args = sys.argv

    f = open(args[1], 'r')
    o = open(args[2], 'w')

    testcases = int(f.readline().strip())

    for t in xrange(1, testcases+1):
        credit = int(f.readline().strip())
        _ = f.readline().strip()
        prices = map(int, f.readline().strip().split())
        
        i, j = solve(credit, prices)
        s = "Case #%d: %i %i\n" % (t, i, j)
        print s
        o.write(s)
