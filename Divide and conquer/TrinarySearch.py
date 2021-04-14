n = int(input())
a=list(map(int, input().split()))
m = int(input())
b=list(map(int, input().split()))
def ternary_search (arr, x):
   count  = 1
   left = 0
   right = len(arr) - 1
   while left <= right:
        i = left + (right - left)//3
        j = left + 2*(right - left)//3 + 1

        if arr[i] == x:
            return i, count

        elif arr[j] == x:
            return j, count

        if x < arr[i]:
            right = i - 1
            count+=1

        elif x > arr[j]:
            left = j + 1
            count+=1

        else:
            left = i + 1
            right = j - 1
            count+=1

   return -1, count

for i in b:
    print(*ternary_search(a, i))