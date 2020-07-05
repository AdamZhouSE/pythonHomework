t=int(input())
res=[]
for i in range(t):
    n=int(input())
    A=input().split(" ")
    this=[]
    for j in range(len(A)):
        A[j]=int(A[j])
    for j in range(len(A)-1):
        yes=True
        for k in range(j+1,len(A)):
            if A[j]<A[k]:
                yes=False
                break
        if yes:
            this.append(A[j])
    this.append(A[-1])
    res.append(this)
for l in res:
    for i in range(len(l)-1):
        print(l[i],end=" ")
    print(l[-1])