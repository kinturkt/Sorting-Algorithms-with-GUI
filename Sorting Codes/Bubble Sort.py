import numpy as np
import time
def bubble_sort(list):

# Swap the elements to arrange in order

    for num in range(0,len(list)):
        for ix in range(len(list)-1):
            if list[ix] > list[ix+1]:
            # Apply swapping formula

                list[ix], list[ix+1] = list[ix+1], list[ix]
    return list

n = int(input("Enter length of an array: "))
list = np.random.randint(1,1000,n)
print("Unsorted List is:", list)
print("-------------------------------------------------------------------------------------------------")

# Calling the function and calculating time
start = time.time()
bubble_sort(list)
print("Sorted List using Bubble Sort is:", list)
print("-------------------------------------------------------------------------------------------------")

end = time.time()
print("Runtime for Bubble Sort is:", end - start, "seconds")