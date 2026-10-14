def reverseArray(arr, n):
    i = 0
    j = n - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

arr = [1, 2, 3, 4, 5]
print(reverseArray(arr, 5))