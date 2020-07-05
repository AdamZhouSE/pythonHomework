import itertools
matrix=[]
t=input()
while(1):
    try:
        a=input().strip()
        if len(a)==8:
            a=a[:len(a)-1]
        a=eval(a)
        if a!=']':
            matrix.append(a)
    except:
        break
r, c, d = len(matrix), len(matrix[0]), ((0, 1), (0, -1), (1, 0), (-1, 0))
def f(i, j):
    t = 0
    for di, dj in d:
        x, y = i + di, j + dj
        if 0 <= x < r and 0 <= y < c and matrix[x][y] > matrix[i][j]:
            t = max(t, f(x, y))
    return t + 1
print(max(f(i, j) for i, j in itertools.product(range(r), range(c))))
