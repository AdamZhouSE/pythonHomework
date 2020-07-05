import math
A=input().split(',')
A=[int(x) for x in A]
def judge(A):
    A.sort()
    return A[0]
print(judge(A))