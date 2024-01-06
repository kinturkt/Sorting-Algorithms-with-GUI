import numpy as np
import time
def quick_sort_using_3_Medians(list):
    if len(list) <= 1:
        return list

    m = len(list) // 2
    pivot = median_of_three(list[0], list[m], list[-1])
    # Partitioning the array into 3 parts
    smaller = [x for x in list if x < pivot]
    equal = [x for x in list if x == pivot]
    larger = [x for x in list if x > pivot]
    return quick_sort_using_3_Medians(smaller) + equal + quick_sort_using_3_Medians(larger)

def median_of_three(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

n = int(input("Enter length of an array: "))
list = np.random.randint(1,1000,n)
print("Unsorted List is:", list)
print("-------------------------------------------------------------------------------------------------")

start = time.time()
sorted_list = quick_sort_using_3_Medians(list)
print("Sorted List is: ",sorted_list)
print("-------------------------------------------------------------------------------------------------")

end = time.time()
print("Runtime for Quick Sort using 3 Medians is:", end - start, "seconds")