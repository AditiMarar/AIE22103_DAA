import numpy as np
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time
sorting_algorithms = {'Bubble Sort': bubble_sort, 'Selection Sort': selection_sort, 'Insertion Sort': insertion_sort}
times = {algo: [] for algo in sorting_algorithms}
arr = np.random.randint(1, 100, size=1000)
for algo, func in sorting_algorithms.items():
    arr_copy = arr.copy()
    time_taken = measure_time(func, arr_copy)
    times[algo] = time_taken
plt.bar(range(len(times)), list(times.values()), align='center')
plt.xticks(range(len(times)), list(times.keys()))
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time')
plt.title('Sorting Algorithms Comparison')
plt.show()
