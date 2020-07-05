'''
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。
3 <= A.length <= 10000
1 <= A[i] <= 10^6
'''

inp = input()
A = inp[1:len(inp)-1].split(",")
A = list(map(int, A))
A.sort()
res = 0
for i in range(len(A) - 3, -1, -1):
    if (A[i+1] + A[i]) > A[i+2]:
        res = A[i] + A[i+1] + A[i+2]
        break
print(res)