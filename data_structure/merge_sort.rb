# Divide and Conquer
# 1. Divide
#  we got array = [10,14,22,1,56,103,21,24,5]

def merge_sort(array)
  if array.length <= 1
    array
  else
    mid = (array.length / 2).floor
    left = merge_sort(array[0..mid-1])
    right = merge_sort(array[mid..array.length-1])
    merge(left, right)
  end
end

# Conquer
def merge(left, right)
  if left.empty?
    right
  elsif right.empty?
    left
  elsif left[0] < right[0]
    [left[0]] + merge(left[1..left.length], right)
  else
    [right[0]] + merge(left, right[1..right.length])
  end
end

x = merge_sort([10,20,5,1])
puts x