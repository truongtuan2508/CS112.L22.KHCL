def convert_matrix_chess(co, r, c):
    ches_x = r-co[0]
    ches_y = chr(97+co[1])
    return str(ches_y)+str(ches_x)

def convert_chess_matrix(co, r, c):
    mat_x = r-int(co[1])
    mat_y = ord(co[0])-97
    return (mat_x, mat_y)

def print_arr(arr, r, c):
    res = ''
    for co in arr:
        coor_ches = convert_matrix_chess(co, r, c)
        res = res+coor_ches+" "
    print(res[:-1])


def backtracking_chess(a, str_res, i, j, m, n, k):
    str_output[k] = (i, j)
    if k == (m*n-1):
        # print(k)
        return str_res, True
    offset = [(-1, 2), (1, 2), (-2, 1), (2, 1),
              (-2, -1), (2, -1), (-1, -2), (1, -2)]

    for d in offset:
        # print(d)
        if 0 <= (i+d[0]) and (i+d[0]) < m and 0 <= (j+d[1]) and (j+d[1]) < n and a[i+d[0]][j+d[1]] == 0:
            # print(i+d[0],j+d[1])
            a[i][j] = 1
            str_res, flag = backtracking_chess(
                a, str_res, i+d[0], j+d[1], m, n, k+1)
            if flag == True:
                return str_res, True
            a[i][j] = 0
    return str_res, False

r, c = input().split()
r = int(r)
c = int(c)
coor = input()
(init_x, init_y) = convert_chess_matrix(coor, r, c)
mat = [[0 for i in range(c)] for j in range(r)]
str_output = [0]*(r*c)

str_res, flag = backtracking_chess(mat, str_output, init_x, init_y, r, c, 0)
# print(flag)
# print(str_res)
if flag == True:
    print_arr(str_res, r, c)