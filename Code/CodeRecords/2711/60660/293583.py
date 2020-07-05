def find (x):
    while x!=p[x]:
        x=p[x]
    return x
def union(x,y):  # 并查集查询连接函数
    p[find(x)]=y
    p[x]=p[find(x)]
def nnm(A):  # O(N^2*M)算法
    n, m = len(A), len(A[0])

    def check(x, y):  # 相似判定函数
        t = 0
        for i in range(m):
            if x[i] != y[i]:
                t += 1
                if t > 2:
                    return False
        return True

    for i in range(n):
        for j in range(i + 1, n):  # 遍历串的两两组合，然后并查集连接
            pi, pj = find(i), find(j)
            if pi != pj and check(A[i], A[j]):
                union(pj,pi)
A=eval(input())
A = [*{*A}]
n, m = len(A), len(A[0])
p = [*range(n)]  # 并查集初始化
nnm(A)
print(len({*map(find, p)}))