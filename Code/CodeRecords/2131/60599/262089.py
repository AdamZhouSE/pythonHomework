"""
我们写一个等差数列[1,2,3,4,5]，找它的所有等差子序列：
[1,2,3] [2,3,4] [3,4,5]
[1,2,3,4][2,3,4,5]
[1,2,3,4,5]
有没有发现什么，总个数是1+2+3！
也就是从1加到n-2，写个求和公式就行了。
所以这道题就变成了找里面所有最大的等差数列了，瞬间就变得很简单了。
"""
A=list(map(int,input().split(',')))
if len(A) < 3:
    print(0)
t = A[1] - A[0]
n = 0
res = []
for i in range(2, len(A)):
    if A[i] - A[i - 1] == t:
        n += 1
    else:
        if n > 0:
            res.append(n)
        n = 0
        t = A[i] - A[i - 1]
if n > 0:
    res.append(n)

print(sum([(i ** 2 + i) // 2 for i in res]))