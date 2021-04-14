from sys import stdin

n = [int(i) for i in stdin.readline().split()]
arr = []
for i in range(n[0]):
    arr.append(int(stdin.readline()))
def partition(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1
def findK(a, k):
    l = 0
    r = len(a) - 1
    split_point = partition(a, l, r)
    if split_point == r - k + 1:
        result = a[split_point]
    elif split_point > r - k + 1:
        result = findK(a[:split_point], k - (r - split_point + 1))
    else:
        result = findK(a[split_point + 1:r + 1], k)
    return result
print(findK(arr, n[1]))