info=input().split()
n=int(info[0])
k=int(info[1])
A=input()
B=input()
q=int(input())
for i in range(q):
    req=[int(x) for x in input().split()]
    T=A[req[0]-1:req[1]]
    P=B[req[2]-1:req[3]]
    curr=0
    l1=len(T)
    l2=len(P)
    sum=0
    while curr < l1:
        if T[curr:curr+l2]==P:
            sum+=k-curr-req[0]
            curr+=l2
        else:curr+=1
    print(sum)