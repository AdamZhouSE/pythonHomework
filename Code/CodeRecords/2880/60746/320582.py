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
        newB.append(int(B[j]))
#print(newB)
def kidnum(N,K,S):
    num=0
    for i in range(N):
        if S[i]<=k:
            num=num+1
        elif S[i]>k:
            break
    for j in range(N-1,-1,-1):
        if S[i]<=k:
            num=num+1
        elif S[i]>k:
            break
    print(num)
    return 0
kidnum(n,k,newB)