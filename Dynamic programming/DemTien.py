n = int(int(input())/10000)
C = [2, 5, 10, 20, 50]


def fBottomUp(X):
    memoi = (X+100)*[0]
    for i in range(2, X+1):
        if i in C:
            memoi[i] = 1
            continue
        B = [memoi[i - x]for x in C]
        if (sum(B) == 0):
            memoi[i] = 0
            continue
        memoi[i] = 1+min([j for j in B if j != 0])
    return memoi[X]


print(fBottomUp(n))