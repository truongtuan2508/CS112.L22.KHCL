def brute_force(ans, i, string, n, c):
    if i >= n:
        print(ans)
        return
    for t in range(i, n):
        if c[i][t]:
            brute_force(ans + string[i:t + 1] + ' ', t + 1, string, n, c)


def main():
    string = input()

    n = len(string)

    c = [([False]*n) for i in range(n)]

    for i in range(n):
        c[i][i] = True
        if (i+1 < n):
            c[i][i+1] = (string[i] == string[i+1])
    for _ in range(2, n):
        for __ in range(0, n-_):
            if string[__] == string[__+_]:
                c[__][__+_] = c[__+1][__+_-1]
    brute_force('', 0, string, n, c)
    return 0


if __name__ == '__main__':
    main()