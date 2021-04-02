n,k=map(int, input().split())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)

def KthLargest(arr, k):
    arr.sort()
    return len(arr)-k
print(arr[KthLargest(arr,k)])
