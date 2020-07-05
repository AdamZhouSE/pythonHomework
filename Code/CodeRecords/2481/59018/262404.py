def jiaoji(N,A,B):
    count=0
    for j in A:
        if j in B:
            count=count+1
    return count        


T=int(input())
for i in range(T):
    N1,M1=input().split(' ')
    N=int(N1)
    M=int(M1)
    A1=input().split(' ')
    B1=input().split(' ')
    A=[int(x) for x in A1]
    B=[int(x) for x in B1]
    print(jiaoji(N,A,B))