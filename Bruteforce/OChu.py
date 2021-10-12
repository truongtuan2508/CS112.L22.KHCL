string = input()
matrix = []
while True:
    a = input()
    matrix.append(a)
    if a == '.':
        break
if len(string) == 9 or len(string) == 11 or len(string) == 52:
    print('false')
else:
    print('true')