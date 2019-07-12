# Merge sort 
# Divide and Conquer
# Divide: divide array by // 2
# Conquert: Sort them
# Combine: Merge them

# Split method for divide array which unsorted
# Merge method if you split small value then merge them together

list = [6,6,2,9,0,1,55,32]

def merge_sort(list):
    if len(list) <= 1:
      return list  

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
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

sorted = merge_sort(list)
print("List: ", sorted)

# Liner search

def linear_search(lst, target):
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return -1

result = linear_search(sorted, 32)
print("Linear search: ", result)


def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

result2 = recursive_binary_search(sorted, 32)
print("Recursive Binary Search: ", result2)


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first - last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

result3 = binary_search(sorted, 10)
print("Normal Binary Search:", result3)