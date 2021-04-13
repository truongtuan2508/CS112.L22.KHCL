t=int(input())
ans=[]
for i in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    arr=(a+b)
    arr.sort()
    ans.append(arr[k])
for i in range(len(ans)):
     print(ans[i])