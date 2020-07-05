import math
B=int(input())
A=input().split(',')
A=[int(x) for x in A]
all=[]
def cal(A,B):
    cons=[]
    for i in range(len(A)):
        for k in range(i, len(A)):
            all.append(A[i:k + 1])
    for i in range(len(all)):
        if(sum(all[i])>=B):
            cons.append(len(all[i]))
    return min(cons)
print(cal(A,B))