def recover(s):
    answers = []
    recover_recur(s, ans=answers)
    
    # answers is a list of list of string fragments
    # so for each list in answer, concat the list with '.'
    answers = [".".join(answer) for answer in answers]
    
    # there may be duplicates
    return list(set(answers))

def recover_recur(s, prefix=[], ans=[]):
    prefixes = valid_prefixes(s)
    
    # already have four fragments but still more in the string
    # this means that that fragments are too small
    # this could be optimized b/c it's kinda wasteful
    if len(prefix) == 4 and prefixes != []:
        return

    if len(prefix) == 4 and prefixes == []:
        ans.append(prefix)
        
    for p, rest in prefixes:
        recover_recur(rest, prefix + [p], ans)

def valid_prefixes(s):
    if s == '':
        return []

    l = []
    for i in xrange(1,4):
        # leading zeroes are not valid fragments, like 01, 002, 00, 000
        if str(int(s[:i])) != s[:i]:
            continue

        # fragments can be at most 255
        if int(s[:i]) < 256:
            l.append((s[:i], s[i:]))
    return l

print recover("12712312112")
print recover("127000")
print recover("25525511135")
print recover("010010")
