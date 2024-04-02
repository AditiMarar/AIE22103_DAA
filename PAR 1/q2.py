import random
import time
import matplotlib.pyplot as plt

# Function to perform linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Function to perform binary search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Generate random array of 10,000 elements in range 1 to 1000
arr = [random.randint(1, 1000) for _ in range(10000)]

# Perform searches and measure time
linear_search_times = []
binary_search_times = []

for _ in range(5):
    search_key = int(input("Enter search key: "))
    
    start_time = time.time()
    linear_search_result = linear_search(arr, search_key)
    linear_search_times.append(time.time() - start_time)
    
    start_time = time.time()
    binary_search_result = binary_search(sorted(arr), search_key)
    binary_search_times.append(time.time() - start_time)

# Plotting
searches = [1, 2, 3, 4, 5]

plt.plot(searches, linear_search_times, label='Linear Search')
plt.plot(searches, binary_search_times, label='Binary Search')
plt.xlabel('Search')
plt.ylabel('Time (seconds)')
plt.title('Time taken by Linear and Binary Searches')
plt.legend()
plt.show()
