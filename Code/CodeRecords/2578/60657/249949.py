import math
A=input().split(',')
A=[int(x) for x in A]
B=int(input())
def judge(A,B):
    A.sort()
    temp=[]
    for i in range(1,A[-1]):
        temp = []
        for k in range(len(A)):
            temp.append(math.ceil(A[k]/i))
        if sum(temp)<=B:
            return i
print(judge(A,B))