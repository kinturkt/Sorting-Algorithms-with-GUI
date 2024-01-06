import sys
import numpy as np
import time

print("************ Welcome to Data Analysis and Algorithm Sorting Project ************")

# Bubble Sort
def bubble_sort(list):
    for num in range(0,len(list)):
        for ix in range(len(list)-1):
            if list[ix] > list[ix+1]:
            # Applying swapping formula

                list[ix], list[ix+1] = list[ix+1], list[ix]
    return list

# Selection Sort
def selection_sort(list):
    for i in range(len(list)):
        min=i
        for j in range (i+1, len(list)):
            if list[min] > list[i]:
                min=j

# Applying swapping formula
        list[i], list[min] = list[min], list[i]
    return list

# Insertion Sort
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
            list[j + 1] = key
    return list

# Heap Sort
def heapify(list, start, end):
    root = start
    while 2*root + 1 <= end:
        child = 2*root + 1
        if child + 1 <= end and list[child] < list[child+1]:
            child += 1
        if child <= end and list[root] < list[child]:
            list[root], list[child] = list[child], list[root]
            root = child
        else:
            return

def heap_sort(list):
    start = len(list) // 2 - 1
    for i in range(start, -1, -1):
        heapify(list, i, len(list)-1)

    for end in range(len(list)-1, 0, -1):
        list[end], list[0] = list[0], list[end]
        heapify(list, 0, end-1)

    return list

# Merge Sort
def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left_half = merge_sort(list[:mid])
    right_half = merge_sort(list[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    res = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res

# Quick Sort
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

# Quick Sort using 3 Medians
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
print("-------------------------------------------------------------------------------------------------")

# User can enter input size for array from 1 to 1000

list = np.random.randint(1, 1000, n)
print("Unsorted List is:", list)
print("-------------------------------------------------------------------------------------------------")

# Calculating runtime complexities of all the algorithms
def runtime():
    s1 = time.time()
    bubble_sort(list)
    e1 = time.time()
    t1 = e1-s1

    s2 = time.time()
    insertion_sort(list)
    e2 = time.time()
    t2 = e2 - s2

    s3 = time.time()
    selection_sort(list)
    e3 = time.time()
    t3 = e3 - s3

    s4 = time.time()
    heap_sort(list)
    e4 = time.time()
    t4 = e4 - s4

    s5 = time.time()
    merge_sort(list)
    e5 = time.time()
    t5 = e5 - s5

    s6 = time.time()
    quick_sort(0, len(list) - 1, list)
    e6 = time.time()
    t6 = e1 - s1

    s7 = time.time()
    quick_sort_using_3_Medians(list)
    e7 = time.time()
    t7 = e7 - s7

    print("\nRuntime Complexity of all algorithms:")
    print("\nRuntime for Bubble Sort is:", t1, "seconds")
    print("\nRuntime for Selection Sort is:", t2, "seconds")
    print("\nRuntime for Insertion Sort is:", t3, "seconds")
    print("\nRuntime for Heap Sort is:", t4, "seconds")
    print("\nRuntime for Merge Sort is:", t5, "seconds")
    print("\nRuntime for Quick Sort is:", t6, "seconds")
    print("\nRuntime for Quick Sort using 3 Medians is:", t7, "seconds")

# Creating a menu to enter user choice of sorting
def menu():
    print("Enter your choice of sorting:")
    choice = input("""
                    1: Bubble Sort
                    2: Selection Sort
                    3: Insertion Sort
                    4: Heap Sort
                    5: Merge Sort
                    6: Quick Sort
                    7: Quick sort using 3 medians
                    8: Invalid option
                    Please enter your choice: """)
    if choice == "1" or choice == "a":
        sorted_list1 = bubble_sort(list)
        print("Sorted List using Bubble Sort is:", sorted_list1)
        runtime()
    elif choice == "2" or choice =="b":
        sorted_list2 = selection_sort(list)
        print("Sorted List using Selection Sort is:", sorted_list2)
        runtime()

    elif choice == "3" or choice =="c":
        sorted_list3 = insertion_sort(list)
        print("Sorted List using Insertion Sort is:", sorted_list3)
        runtime()

    elif choice == "4" or choice =="d":
        sorted_list4 = heap_sort(list)
        print("Sorted List using Heap Sort is:",sorted_list4)
        runtime()

    elif choice == "5" or choice =="e":
        sorted_list5 = merge_sort(list)
        print("Sorted List using Merge Sort is:",sorted_list5)
        runtime()

    elif choice == "6" or choice =="f":
        sorted_list6 = quick_sort(0, len(list) - 1, list)
        print("Sorted List using Quick Sort is:",sorted_list6)
        runtime()

    elif choice == "7" or choice =="g":
        sorted_list7 = quick_sort_using_3_Medians(list)
        print("Sorted List using Quick Sort using 3 Medians is:",sorted_list7)
        runtime()

    elif choice=="8" or choice=="q":
        print("Wrong choice selected, please select correct choice and Try again.")
        sys.exit()
    else:
        print("Invalid Selection!!!! Please select your input from above options only")
        print("Please try again")

    sys.exit()
menu()
print("xxxxxxxxxxxxx-------------------xxxxxxxxxxxxx-------------------xxxxxxxxxxxxx-------------------xxxxxxxxxxxxx")