# Write a naive fibinacci function recursively. It should look a lot like below, but you'll need to add some code: (Bonus for later: memoize this) Explain it to someone else.
# def fib(n):
#     return fib(n-1) + fib(n-2)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print "Fib: "
print fib(0) == 0
print fib(1) == 1
print fib(2) == 1
print fib(3) == 2
print fib(4) == 3
print fib(5) == 5
print fib(6) == 8
print 

# Finish this code for finding the largest number in a list:
# def max(numbers, largest_so_far=0):
#     if numbers == []:
#         return largest_so_far
#     next_num = numbers[0]
#     if next_num > largest_so_far:
#         return ?
#     else:
#         return ?

def max(numbers, largest_so_far=0):
    if numbers == []:
        return largest_so_far
    next_num = numbers[0]
    if next_num > largest_so_far:
        return max(numbers[1:], next_num)
    else:
        return max(numbers[1:], largest_so_far)

print "Largest num in list: "
print max([]) == 0
print max(range(10)) == 9
print max(range(100)) == 99
print max([10,12, 2, 3, 4]) == 12
print 

# Using no loops (for, while, etc.), and no global variables, write a function that returns the sum of a list: Also, no cheating and calling methods that do significant work for you (i.e. sum(), reduce(), etc. are all off limits).
# sum([1, 2, 3, 4, 5]) -> 15
# sum([]) -> 0

def sum(nums, so_far=0):
    if nums == []:
        return so_far
    return sum(nums[1:], so_far + nums[0])

print "sum: " 
print sum([1, 2, 3, 4, 5]) == 15
print sum(range(5)) == 10
print sum([]) == 0
print 

# Again, using no loops, no global variables, and no calling asking for the length of the array, write a function that returns the last index of a given input in a list. Negative one gets returned if the element doesn't occur in the list. Don't go from the back (for why not, see "Linked List Aside") Feel free to change to the signature of the function or use a helper function with a different signature!
# lastIndexOf(5, [1, 2, 4, 6, 5, 2, 7]) -> 4
# lastIndexOf(5, [1, 2, 4, 6, 2, 7]) -> -1
# lastIndexOf(5, [1, 2, 5, 4, 6, 5, 2, 7]) -> 5

def lastIndexOf(num, list, last_idx=-1, curr_idx=0):
    if list == []:
        return last_idx
    
    new_last = last_idx
    if list[0] == num:
        new_last = curr_idx
    return lastIndexOf(num, list[1:], new_last, curr_idx + 1)

print "last index of: " 
print lastIndexOf(5, [1, 2, 4, 6, 5, 2, 7]) == 4
print lastIndexOf(5, [1, 2, 4, 6, 2, 7]) == -1
print lastIndexOf(5, [1, 2, 5, 4, 6, 5, 2, 7]) == 5 
print

# Write a recursive function to compute the sum of a binary tree of numbers. Here's an example of a tree:
# class Node(object):
#     def __init__(self, value, l=None, r=None):
#         self.value = value
#         self.left = l
#         self.right = r

# tree1 = Node(1, 
#              Node(2,
#                   Node(3),
#                   Node(4)),
#              Node(5,
#                   Node(6),
#                   Node(7)))

# tree2 = Node(1,
#              Node(2, 
#                   Node(3)),
#              Node(4))
# If this is confusing, see check out a visualization of this data structure: visualisation 
# Print the elements of a tree with such a structure depth-first (in the order 1, 2, 3, 4, 5, 6, 7 for the tree1)

class Node(object):
    def __init__(self, value, l=None, r=None):
        self.value = value
        self.left = l
        self.right = r

    def __str__(self):
        left_str = "" if self.left is None else str(self.left)
        right_str = "" if self.right is None else str(self.right)
        
        return str(self.value) + left_str + right_str

tree1 = Node(1, 
             Node(2,
                  Node(3),
                  Node(4)),
             Node(5,
                  Node(6),
                  Node(7)))

tree2 = Node(1,
             Node(2, 
                  Node(3)),
             Node(4))

def bt_sum(tree):
    if tree == None:
        return 0
    return tree.value + bt_sum(tree.left) + bt_sum(tree.right)

print "bt sum: " 
print bt_sum(None) == 0
print bt_sum(tree1) == 28
print bt_sum(tree2) == 10
print 

print "print trees depth first"
print str(tree1) == "1234567"
print str(tree2) == "1234"
print 

# Generate all the reorderings of a set of letters.
def permutations(str, prefix=""):
    if len(str) == 0:
        return [prefix]
    
    list = []
    for index, char in enumerate(str):
        list.append(permutations(str[:index] + str[index + 1:], prefix + char))
    return flatten(list)

# helper just to make the output look nicer
def flatten(list):
    return [item for sublist in list for item in sublist]

print "perms: " 
print permutations("a") == ['a']
print permutations("B") == ['B']
print permutations("aB") == ['aB', 'Ba'] 
print permutations("aBC") == ['aBC', 'aCB', 'BaC', 'BCa', 'CaB', 'CBa']
print 

# List all of the series' of letters (non-dictionary words, 'asd' and 'w' count) that can be formed with some scrabble tiles on a blank board. (In scrabble, you don't have to use all your tiles at once)

def scrabble(tiles):
    combs = combinations(tiles);
    
#    return list(set([perm for comb in combs for perm in permutations(comb)]))
    return list(set(flatten(map(permutations, combs))))
    
def combinations(tiles):
    if len(tiles) == 0:
        return []
    
    l = [[tiles]]
    for i in xrange(len(tiles)):
        l.append(scrabble(tiles[:i] + tiles[i + 1:]))
        
    return list(set(flatten(l)))

print "scrabble: " 
print scrabble("ab") == ['a', 'ab', 'b', 'ba']
print scrabble("abc") == ['a', 'acb', 'c', 'abc', 'ba', 'bc', 'cb', 'ca', 'bca', 'cba', 'bac', 'cab', 'b', 'ab', 'ac']
print 

def scrabble_dict(tiles, dict):
    possible = scrabble(tiles)
    return filter(lambda x: x in dict, possible)

# A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Write a function that, given the length of the staircase, tells you how many ways there are to go up the steps.

def staircase(steps, ways=0):
    if steps == 0:
        return ways + 1
        
    one = staircase(steps -1, ways)
    two = 0 if steps - 2 < 0 else staircase(steps - 2, ways)
    three = 0 if steps - 3 < 0 else staircase(steps - 3, ways)

    return one + two + three

print "staircase: " 
print staircase(0) == 1
print staircase(1) == 1
print staircase(2) == 2
print staircase(3) == 4
print staircase(4) == 7
print

# project euler 15
# How many ways are there for a taxi driver to get from the top left of a grid city to the bottom right? The city is exactly 10 blocks in each direction, all streets are two ways, and you know the city well enough that you'd balk if the driver actually went drove away from the goal - so never up or left, only right and down.

def taxi(grid_dimen):
    return taxiHelper((0,0), (grid_dimen, grid_dimen))
    
def taxiHelper(curr, dest, ways=0):
    if curr == dest:
        return ways + 1

    dest_x, dest_y = dest
    curr_x, curr_y = curr    
    
    right_ways = 0 if curr_x >= dest_x else taxiHelper((curr_x + 1, curr_y), dest, ways) 
    
    down_ways = 0 if curr_y >= dest_y else taxiHelper((curr_x, curr_y + 1), dest, ways)
    
    return right_ways + down_ways

print "taxi: " 
print taxi(10)
