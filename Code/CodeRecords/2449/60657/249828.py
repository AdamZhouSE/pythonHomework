import math
A=input().split(',')
B=input()
def judge(A,B):
    if A.count(B)!=0:
        return A.index(B)
    else:
        return -1
print(judge(A,B))