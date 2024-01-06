import numpy as np
import time

def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left_half = merge_sort(list[:mid])
    right_half = merge_sort(list[mid:])

    return merge(left_half, right_half)

def merge(left_half, right_half):
    res = []
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            res.append(left_half[i])
            i = i + 1
        else:
            res.append(right_half[j])
            j = j + 1

    res.extend(left_half[i:])
    res.extend(right_half[j:])
    return res

n = int(input("Enter length of an array: "))
list = np.random.randint(1,1000,n)
print("Unsorted List is:", list)
print("-------------------------------------------------------------------------------------------------")

start = time.time()
print("Sorted List using Merge Sort is", merge_sort(list))
print("-------------------------------------------------------------------------------------------------")

end = time.time()
print("Runtime for Merge Sort is:", end - start, "seconds")