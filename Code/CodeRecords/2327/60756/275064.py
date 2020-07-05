S=list(input())
N=len(S)
X=[]
L=0
R=N
for i in S:
    if i=="I":
        X.append(L)
        L+=1
    else:
        X.append(R)
        R-=1
X.append(R)
print(X)