import math
A=input().split(',')
B=input()
def judge(A,B):
    cons=[]
    if(A.count(B)!=0):
        cons.append(A.index(B))
        A.reverse()
        cons.append(len(A)-A.index(B)-1)
    else:
        cons=[-1,-1]
    return cons
print(judge(A,B))