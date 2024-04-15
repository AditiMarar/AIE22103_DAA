def pylons(k, arr):
    n = len(arr)
    count = 0
    i = 0
    power_plant_indices = []

    while i < n:
        j = min(i + k - 1, n - 1)
        while j >= i - k + 1 and arr[j] == 0:
            j -= 1
        if j < i - k + 1:
            return -1, []
        count += 1
        power_plant_indices.append(j)
        i = j + k

    return count, power_plant_indices
print(pylons(2,[0,1,1,1,1,0]))
