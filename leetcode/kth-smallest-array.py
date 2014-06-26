# Find the kth smallest element in an unsorted array

# partition like you would with quicksort and use size of the partitions to determine location

def kthSmallest(k, arr):
    if arr == []:
        return "ERROR: empty arr"

    pivot = arr[0]
    strict_less, great_eq = partition(lambda x: x < pivot, arr[1:])

    num_less = len(strict_less)
    num_great = len(great_eq)

    if k == 0 and num_less == 0:
        return pivot
    if k == num_less + 1:
        return pivot
    if num_less <= k:
        return kthSmallest(k - num_less - 1, great_eq)
    else:
        return kthSmallest(k , strict_less)


# returns a pair of lists; the first list contains 
# all the elems where cond(elem) is true
def partition(cond, arr):
    a = []
    b = []
    for elem in arr:
        if cond(elem):
            a.append(elem)
        else:
            b.append(elem)
    return (a, b)

print kthSmallest(2, [1,2,3,4,5]) # 2
print kthSmallest(0, [1,2,3,4,5]) # 1
print kthSmallest(5, [1,2,3,4,5]) # 5
print kthSmallest(3, [3, 5, 1, 9, 2, 10]) # 3
print kthSmallest(2, [1, 1, 2])
print kthSmallest(2, [1, 2, 2])
