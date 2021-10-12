open_count = 0
open_diff = 0
solution_count = 0

def printS(s):
    temp=""
    for i in range(len(s)):
        temp+=s[i]
    print(temp)


def check(i):
    global open_count
    global open_diff
    global solution
    global solution_count
    global n
    global n_h
    if open_count < n_h:
        solution[i] = "("
        open_count += 1
        open_diff += 1
        check(i + 1)
        open_count -= 1
        open_diff -= 1

    if open_diff > 0:
        solution[i] = ")"
        open_diff -= 1
        if i == n - 1:
            printS(solution)
            solution_count += 1
        else:
            check(i + 1)
        open_diff += 1


n = int(input())
n_h = n
n *= 2
solution = ["" for x in range(n)]
check(0)