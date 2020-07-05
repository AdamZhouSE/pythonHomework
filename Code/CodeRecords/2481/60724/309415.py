T=int(input())
for i in range(T):
    string=input().split(" ")
    N=int(string[0])
    M=int(string[1])
    A=input().split(" ")
    B=input().split(" ")
    result=[]
    for i in range(N):
        if A[i] in B:
            result.append(A[i])
    result=list(set(result))
    print(len(result))