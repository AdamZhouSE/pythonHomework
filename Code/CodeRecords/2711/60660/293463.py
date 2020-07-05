def uni(x: int):  # 并查集查询连接函数
    if x != p[x]:
        p[x] =uni(p[x])
    return p[x]


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
            pi, pj = uni(i), uni(j)
            if pi != pj and check(A[i], A[j]):
                p[pj] = pi
A=eval(input())
A = [*{*A}]  # 字符串去重，这个是题目给的坑
n, m = len(A), len(A[0])
p = [*range(n)]  # 并查集初始化
nnm(A)  # 选择方案
print( len({*map(uni, p)}))  # 并查集去重输出长度