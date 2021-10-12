m, n = [int(i) for i in input().split()]
cal = [[0]*n]*2
for x in range(m):
    if x == 0 :
        cal[0] = [int(i) for i in input().split()]
        for i in range (n):
            if i==0:
                cal[0][i]=1
            elif cal[0][i-1]==0: 
                cal[0][i]=0
    else:
        cal[1] = [int(i) for i in input().split()]
        for y in range(n):
            if y == 0 and cal[1][0] != 0:
                cal[0][y] = cal[0][0]
            elif cal[1][y] == 0:
                cal[0][y] = 0
            else:
                cal[0][y] = cal[0][y] + cal[0][y-1]
print(cal[0][n-1] % (10000000000001))