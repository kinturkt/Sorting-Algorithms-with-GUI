import numpy as np
import time

def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end

def quick_sort(start, end, array):
    if start < end:
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

n = int(input("Enter length of an array: "))
list = np.random.randint(1, 1000, n)
print("Unsorted List is:", list)

# Calling the function and calculating time
start = time.time()
quick_sort(0, len(list) - 1, list)
end = time.time()
print("-------------------------------------------------------------------------------------------------")
print("Sorted list is:", list)
print("-------------------------------------------------------------------------------------------------")
print("Runtime for Quick Sort is:", end - start, "seconds")