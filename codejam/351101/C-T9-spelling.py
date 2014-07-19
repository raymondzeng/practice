import sys

alph   = "abcdefghijklmnopqrstuvwxyz "
phone  = "222333444555666777788899990" # number corresp. to char
offset = "123123123123123123412312341" # how many taps of that number
 
def solve(str):
    ans = ""
    for char in str:
        idx = alph.index(char)
        key = phone[idx]
        taps = offset[idx]
        to_append = key * int(taps)
        
        if len(ans) != 0 and ans[-1] == key:
            ans += " "
        
        ans += to_append
            
    return ans

    
if __name__ == "__main__":
    args = sys.argv
    
    f = open(args[1], 'r')
    o = open(args[2], 'w')

    testcases = int(f.readline().strip())

    for t in xrange(1, testcases+1):
        l = f.readline().rstrip("\n")
    
        res = solve(l)
        s = "Case #%d: %s\n" % (t, res)
        o.write(s)
