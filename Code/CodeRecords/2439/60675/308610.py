k = int(input())
mat = []
for i in range(k):
    mat.append([0 for _ in range(k)])
for i in range(0, k-1):
    m, n, weight = [int(x) for x in input().split()]
    mat[m-1][n-1] = weight

T = int(input())
ans = []
for i in range(T):
    start, end = [int(x) for x in input().split()]
    if start == end:
        ans.append(0)
        continue
    sum_weight = 0
    start -= 1
    end -= 1
    while True:
        flag = False
        for j in range(0, k):
            if mat[start][j] != 0:
                sum_weight ^= mat[start][j]
                if j == end:
                    flag = True
                    break
                start = j
        if flag:
            break
    ans.append(sum_weight)
for i in ans:
    print(i)