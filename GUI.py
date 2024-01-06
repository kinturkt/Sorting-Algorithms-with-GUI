import tkinter as tk
from tkinter import messagebox
import numpy as np
from easygui import integerbox
import time

# Bubble Sort
def bubble_sort(my_list):
    for num in range(len(my_list)):
        for ix in range(len(my_list) - 1):
            if my_list[ix] > my_list[ix + 1]:
                my_list[ix], my_list[ix + 1] = my_list[ix + 1], my_list[ix]
    return my_list

# Selection Sort
def selection_sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list


# Insertion Sort
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

# Heap Sort
def heapify(arr, start, end):
    root = start
    while 2 * root + 1 <= end:
        child = 2 * root + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

def heap_sort(arr):
    start = len(arr) // 2 - 1
    for i in range(start, -1, -1):
        heapify(arr, i, len(arr) - 1)

    for end in range(len(arr) - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        heapify(arr, 0, end - 1)
    return arr

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
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Quick Sort using 3 Medians
def quick_sort_using_3_Medians(list):
    if len(list) <= 1:
        return list

    m = len(list) // 2
    pivot = median_of_three(list[0], list[m], list[-1])
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

ip = "Enter array input size:"
n = integerbox(ip, "Input", None, 0, 2500)

# User can enter input size for array from 1 to 2500
# So, if the user enters value greater than 2500, it will show error
list = np.random.randint(1, 2500, n)

# Function to print Unsorted List
def unsorted_list():
    global list
    # list = np.random.randint(1, 2500, n)
    unsorted_str = "Unsorted List:\n" + ', '.join(map(str, list))
    messagebox.showinfo("Unsorted List", unsorted_str)

# Function to print Sorted List
def sorted_list(sorting_algorithm):
    sorting_functions = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Heap Sort": heap_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Quick Sort by 3 Medians": quick_sort_using_3_Medians
    }
    sorting_function = sorting_functions.get(sorting_algorithm)

    if sorting_function is not None:
        list_to_sort = list.copy()
        sort_list = sorting_function(list_to_sort)
        sorted_str = "Sorted List using " + sorting_algorithm + ":\n" + ', '.join(map(str, sort_list))
        messagebox.showinfo(f"{sorting_algorithm} Sorted .....33336List", sorted_str)
    else:
        messagebox.showerror("Error", "Invalid sorting algorithm selection")

# Function to print Runtime complexity
def show_runtime(selected_algorithm=None):
    list_to_sort = list.copy()

    times = {}                                    # Create an empty set
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Heap Sort": heap_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": lambda list: quick_sort(list),
        "Quick Sort by 3 Medians": quick_sort_using_3_Medians
    }

    for algo_name, algo_func in algorithms.items():
        s = start_time = time.time()
        algo_func(list_to_sort.copy())
        e= end_time = time.time()
        execution_time = e-s
        times[algo_name] = execution_time

        if algo_name == selected_algorithm:
            messagebox.showinfo(f"{algo_name} Runtime", f"Runtime for {algo_name}: {times[algo_name]:.6f} seconds")

    if selected_algorithm is None:
        runtime_str = "\n".join([f"{alg}: {times[alg]:.6f} seconds" for alg in algorithms])
        messagebox.showinfo("Runtime Complexities", runtime_str)

# GUI Setup
root = tk.Tk()          # root is the main window of Tkinter module
root.geometry("500x300")
root['bg'] = 'light yellow'
root.title("GUI for Design Analysis and Algorithm Project")

selected_algorithm = tk.StringVar()
selected_algorithm.set("Bubble Sort")  # If no selection is done, then Default sorting algorithm will be Bubble Sort.

# Tkinter Label is a widget that is used to implement display boxes where you can place text or images.

label_unsorted_list = tk.Label(root, text="Click to generate Unsorted List :")
label_unsorted_list.grid(column=0, row=0)

label_unsorted_list1 = tk.Label(root, text="Select your desired Algorithm :")
label_unsorted_list1.grid(column=0, row=4)

label_sorted_list2 = tk.Label(root, text="Click to view Sorted List :")
label_sorted_list2.grid(column=0, row=8)

label_runtime_list3 = tk.Label(root, text="Click to get Time Complexities of all Algorithms:")
label_runtime_list3.grid(column=0, row=12)

label_exit_list4 = tk.Label(root, text="To close the GUI, click the Exit button:")
label_exit_list4.grid(column=0, row=20)

btn_1 = tk.Button(root, text="Random Unsorted List", command=unsorted_list)
btn_1.grid(column=1,row=0)

btn_2 = tk.Button(root, text="Sorted List", command=lambda: sorted_list(selected_algorithm.get()))
btn_2.grid(column=1,row=8)

dropdown_btn = tk.OptionMenu(root, selected_algorithm,
                             "Bubble Sort", "Selection Sort", "Insertion Sort", "Heap Sort", "Merge Sort",
                             "Quick Sort", "Quick Sort by 3 Medians")
dropdown_btn.grid(column=1, row=4)

btn_3 = tk.Button(root, text="Runtime", command=show_runtime)
btn_3.grid(column=1, row=12)
def exit_app():
    root.destroy()

exit_btn = tk.Button(root, text="Exit", command=exit_app)
exit_btn.grid(column=1, row=20)

root.mainloop()    # It is a method on the main window which we execute when we want to run our application
