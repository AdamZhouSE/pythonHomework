A=list(input())
nA=len(A)
newA=[]
for i in range(nA):
    if A[i].isdecimal():
        newA.append(int(A[i]))
n=newA[0]
k=newA[1]
#print('n=',n,'k=',k)
B=list(input())
nB=len(B)
newB=[]
for j in range(nB):
    if B[j].isdecimal():
        newB.append(int(B[i]))
def bestbucket(K,S):
    n=len(S)
    new=[]
    for i in range(n):
        if K%(S[i])==0:
            new.append(S[i])
    best=max(new)
    minitime=int(k/best)
    print(minitime)
    return 0
bestbucket(k,newB)