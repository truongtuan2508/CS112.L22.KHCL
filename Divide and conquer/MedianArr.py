t=int(input())
ans=[]
for i in range(t):
    na,nb=map(int,input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    arr=(a+b)
    arr.sort()
    if (na+nb)<3:
        ans.append((arr[0]+arr[1])/2)
    else:
        if(na+nb)%2==0:
            mid=int((na+nb)/2)
            temp= (arr[mid]+arr[mid-1])/2
            ans.append(temp)
        else:
            ans.append(arr[(na+nb)//2])
for i in range(len(ans)):
    print(f'{ans[i]:g}')