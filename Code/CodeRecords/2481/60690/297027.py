t=int(input())
res=[]
for i in range(t):
    s=input().split(" ")
    n=int(s[0])
    m=int(s[1])
    A=input().split(" ")
    B=input().split(" ")
    for j in range(len(A)):A[j]=int(A[j])
    for j in range(len(B)): B[j] = int(B[j])
    union=[]
    for e in A:
        if e in B and e not in union:
            union.append(e)
    for e in B:
        if e in A and e not in union:
            union.append(e)
    res.append(len(union))
for e in res:print(e)