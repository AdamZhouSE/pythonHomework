'''
给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。
在此过程之后，我们得到一些数组 B。
返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
'''

inp = input()
A = inp.split(',')
k = int(input())

A.sort()
minA = int(A[0])
maxA = int(A[-1])
res = maxA - minA
for i in range(len(A) - 1):
    a, b = int(A[i]), int(A[i + 1])
    res = min(res, max(maxA - k, a + k) - min(minA + k, b - k))
print(res)
