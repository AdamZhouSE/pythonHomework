import math
A=input().split(',')
want=[]
for i in range(len(A)):
    start=0
    for k  in range(len(A[i])):
        if A[i][k]=='"':
            start=k+1
            break
    want.append(A[i][start:-1])
cons1=[]
for i in want[0]:
    cons1.append(i)
cons2=[]
for i in want[1]:
    cons2.append(i)
cons2.sort()
cons1.sort()
def judge(A,B):
    if A==B:
        return 'true'
    else:
        return 'false'
print(judge(cons1,cons2))