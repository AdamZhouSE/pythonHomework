A=input()
B=input()
newB=[]
for i in B:
    if i!=' ':
        newB.append(i)
newA=[]

for i in A:
    if i!=' ':
        newA.append(i)

def fourSumCount(A,B):
    for i in B:
        if A.count(i)==0:
                return 'NO'
        A[A.index(i)]=0
    return 'YES'
print(fourSumCount(newA,newB),end='')