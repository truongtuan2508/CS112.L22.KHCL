def range_prime(n):
    numbers = [True] * n
    for i in range(2, int(n**(1/2)+1)):
        k = i * 2
        while k < n:
            numbers[k] = False
            k = k + i
    first = [i for i in range(2, n // 2 + 1) if numbers[i]]
    second = [i for i in range(n - 2, n // 2 - 1, -1) if numbers[i]]

    return first, second


def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


n = int(input())
count = 0
first, second = range_prime(n)
x = len(first)
y = len(second)

if x > y:
    for i in range(y):
        if binarySearch(first, 0, x - 1, n - second[i]) != -1:
            count += 1

print(count)