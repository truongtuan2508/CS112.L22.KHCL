def backtracking(arr1, arr2, arr3, i, n, dtb, a1, a2):
    if i == n:
        for k in arr2:  
            print(k, end = " ")
        print()
        return
    for j in arr3:
        arr2[i] = j 
        a3 = a1 + arr1[i] * arr2[i]
        a4 = a2 + arr1[i]
        max_values = a3 + 10 * (1 - a4)
        min_values = a3 + 0.25 * (1 - a4)
        if round(max_values + 0.001, 1) < dtb or round(min_values + 0.001, 1) > dtb:
            continue
        else:
            backtracking(arr1, arr2, arr3, i + 1, n, dtb, a3, a4)
    
n = int(input())
he_so = []
for i in range(n):
    he_so.append(int(input())/100)
dtb = float(input())
arr = [0]*n
arr3 =  [0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,
            3,3.25,3.5,3.75,4,4.25,4.5,4.75,5,5.25,5.5,5.75,
            6,6.25,6.5,6.75,7,7.25,7.5,7.75,8,8.25,8.5,8.75,
            9,9.25,9.5,9.75,10] 
backtracking(he_so, arr, arr3, 0, n, dtb, 0, 0)