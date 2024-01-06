import numpy as np
import time

def heapify(arr, start, end):
    root = start
    while 2*root + 1 <= end:
        child = 2*root + 1
        if child + 1 <= end and arr[child] < arr[child+1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

def heap_sort(arr):
    start = len(arr) // 2 - 1
    for i in range(start, -1, -1):
        heapify(arr, i, len(arr)-1)

    for end in range(len(arr)-1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        heapify(arr, 0, end-1)

    return arr

n = int(input("Enter length of an array: "))
arr = np.random.randint(1,1000,n)
print("Unsorted List is:", arr)
print("-------------------------------------------------------------------------------------------------")

start = time.time()
print("Sorted List using Heap Sort is", heap_sort(arr))
print("-------------------------------------------------------------------------------------------------")

end = time.time()
print("Runtime for Heap Sort is:", end - start, "seconds")