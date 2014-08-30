# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution:
    # @return an integer
    def reverse(self, x):
        negative = x < 0
        s = str(abs(x))
        reverse_s = s[::-1]
        i = int(reverse_s)
        if negative:
            i *= -1
        return i
