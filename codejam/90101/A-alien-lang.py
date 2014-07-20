import sys
import re

def prefix_in_list(prefix, l):
    truths = [word.startswith(prefix) for word in l]
    return reduce(lambda x, y: x or y, truths)
    
def combinations(parts, dict, prefix=""):
    if len(parts) == 0:
        return [prefix]

    part = parts[0]
    if isinstance(part, str):
        new_prefix = prefix + part
        if not prefix_in_list(new_prefix, dict):
            return []
        return combinations(parts[1:], dict, prefix=new_prefix)
    
    combos = []
    for choice in part:
        if not prefix_in_list(prefix+choice, dict):
            continue
        combos.extend(combinations(parts[1:], dict, prefix=prefix+choice))

    return combos
        

def solve(str, dict, l):
    print str
    variables = re.findall("\((.+?)\)", str)
    parts = []
    for variable in variables:
        idx = str.find("(" + variable)
        parts.extend(list(str[:idx]))
        parts.append(list(variable))
        str = str[idx + len(variable) + 2:]
    
    parts.append(str)

    possible = combinations(parts, dict)

    possible = [x for x in possible if x in dict]
    print len(possible)
    return len(possible)


if __name__ == "__main__":
    args = sys.argv
    
    f = open(args[1], 'r')
    o = open(args[2], 'w')

    l, d, testcases = map(int, f.readline().strip().split())
    
    dict = []
    for _ in xrange(d):
        dict.append(f.readline().strip())

    for t in xrange(1, testcases+1):
        pattern = f.readline().strip()
    
        res = solve(pattern, dict, l)
        s = "Case #%d: %s\n" % (t, res)
        o.write(s)
