
def matrix_compute(l, k, t)->int:
    s = 0
    for i_i in range(l, l+t):
        for j_j in range(k, k+t):
            s += mat[i_i][j_j]
    return s


m = int(input())
n = 0
mat = list()
for i in range(m):
    l_n = [int(x) for x in input().split(",")]
    mat.append(l_n)
threshold = int(input())
n = len(mat[0])
max_ = 0
for i in range(min(m, n)+1):
    for j in range(0, m - i + 1):
        for k in range(0, n - i + 1):
            if matrix_compute(j, k, i) <= threshold:
                max_ = max(max_, i)
print(max_)