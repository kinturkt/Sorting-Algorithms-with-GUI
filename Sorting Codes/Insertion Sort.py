import numpy as np
import time

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1 
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
            list[j + 1] = key
    return list

n = int(input("Enter length of an array: "))
list = np.random.randint(1,1000,n,dtype=int)
print("Unsorted list is :",list)
print("-------------------------------------------------------------------------------------------------")

start = time.time()
insertion_sort(list)
print("Sorted list using Insertion Sort is:", list)
print("-------------------------------------------------------------------------------------------------")

end = time.time()
print("Runtime for Insertion Sort is:",end - start, "seconds")