def atoi(str):
        digits = list(str.strip())
        
        print digits

        if len(digits) == 0:
                return 0
                
        negate = False
        
        if digits[0] == '-':
                print "negate"
                negate = True
                digits = digits[1:]
        elif digits[0] == '+':
                digits = digits[1:]
                
        num = 0
        for digit in digits:
                if not digit.isdigit():
                        break;
                        num = num * 10 + int(digit)
                        
        if negate:
                num *= -1

        return num
