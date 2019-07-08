# Binary search

# Merge sort
# Split 2 small array and smaller until got single array

def merge_sort(list):
    """
    Sorts a list in ascending order
    Return a new sorted list
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Take O(kn log n)
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted ist at midpoint sublists
    Return two sublists - left and right
    Takes overall O(log n) time

    O(n log n)
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    Run in overall O(n) time
    """

    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54, 20, 52, 1, 77, 35, 56, 68]
l = merge_sort(alist)

print(verify_sorted(alist))
print(verify_sorted(l))



"""
-in a perfect world you'd have to do log n merges of size n, n/2, n/4 ... (or better said 1, 2, 3 ... n/4, n/2, n - they can't be parallelized), which gives O(n). It still is O(n log n). In not-so-perfect-world you don't have infinite number of processors and context-switching and synchronization offsets any potential gains.

-Space complexity is always Ω(n) as you have to store the elements somewhere. Additional space complexity can be O(n) in an implementation using arrays and O(1) in linked list implementations. In practice implementations using lists need additional space for list pointers, so unless you already have the list in memory it shouldn't matter.

- edit if you count stack frames, then it's O(n)+ O(log n) , so still O(n) in case of arrays. In case of lists it's O(log n) additional memory.

- Lists only need some pointers changed during the merge process. That requires constant additional memory.

- That's why in merge-sort complexity analysis people mention 'additional space requirement' or things like that. It's obvious that you have to store the elements somewhere, but it's always better to mention 'additional memory' to keep purists at bay.
"""