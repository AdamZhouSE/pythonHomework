import math
s = ''  # 字符串
sa = []    # 排名为i的后缀字符串编号, 从1-n
x = []  # 第一关键字
y = []  # 第二关键字
c = []  # 桶排序
n = 0
m = 0


def SA():
    global m, y, x, n, sa, c, s
    # 桶排序
    for i in range(n):
        x[i+1] = ord(s[i])
        c[x[i+1]] += 1
    for i in range(2, m+1):  # 对前缀求和, 得出x[i]的排序
        c[i] += c[i-1]
    for i in range(n,0,-1):     # 第一关键字桶排序, 得到sa数组
        sa[c[x[i]]] = i
        c[x[i]] -= 1

    # 倍增算法
    k = 1
    while k <= n:
        num = 0
        for i in range(n+1-k, n+1):  # 对于后k个元素, 已经排好序
            num += 1
            y[num] = i
        for i in range(1, n+1):  # 如果可以作为第二关键字, 放在第一关键字中, 此时y[i]为第二关键字排序结果
            if sa[i] > k:
                num += 1
                y[num] = sa[i] - k

        # 对y[i]桶排序
        for i in range(1, m+1):     # 更新桶
            c[i] = 0
        for i in range(1, n + 1):
            c[x[i]] += 1
        for i in range(2, m+1):
            c[i] += c[i-1]
        for i in range(n,0,-1):
            sa[c[x[y[i]]]] = y[i]
            c[x[y[i]]] -= 1
            y[i] = 0

        # 更新x[i]
        temp = x.copy()
        num = 1
        x[sa[1]] = 1
        for i in range(2, n+1):
            if temp[sa[i]] == temp[sa[i-1]] and temp[sa[i] + k] == temp[sa[i-1] + k]:
                x[sa[i]] = num
            else:
                num += 1
                x[sa[i]] = num
        if num == n:
            break
        m = num
        k = 2 * k
    # 打印
    for i in range(1, n):
        print(sa[i],end=' ')
    print(sa[n])
    return


if __name__ == '__main__':
    s = input()
    n = len(s)
    m = 122
    sa = [0 for i in range(n + int(math.log(n,2)) + 1)]
    x = sa.copy()
    y = sa.copy()
    c = [0 for i in range(m + int(math.log(m, 2)) + 1)]
    SA()