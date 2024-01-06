import numpy as np
import time

def selection_sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j

        # Apply swapping formulas
        list[i], list[min] = list[min], list[i]
    return list

n = int(input("Enter length of an array: "))
list = np.random.randint(1,1000,n)

print("Unsorted list is: ", list)
print("-------------------------------------------------------------------------------------------------")

start = time.time()
print("Sorted list is:", selection_sort(list))
print("-------------------------------------------------------------------------------------------------")

end = time.time()
print("Runtime for Selection Sort is:", end - start, "seconds")