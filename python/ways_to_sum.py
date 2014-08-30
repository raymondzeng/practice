def f(money, bills, sofar=[]):
    if money < 0:
        return 0
    if money == 0:
        print sofar
        return 1

    if len(bills) == 0:
        return 0

    return f(money - bills[0], bills, sofar + [bills[0]]) + f(money, bills[1:], sofar)

print f(100, [1,5,10,25])

