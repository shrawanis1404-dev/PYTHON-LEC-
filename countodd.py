def countOdd(arr, n):
    count = 0
    for i in range(n):
        if arr[i] % 2 != 0:
            count += 1
    return count
arr = [1, 2, 3, 4, 5, 7]
print(countOdd(arr, 6))