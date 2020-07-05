def Test():
    N,X,Y=map(int,input().split())
    A = eval("[" + input().strip().replace(" ", ",") + "]")
    B = eval("[" + input().strip().replace(" ", ",") + "]")
    result=0
    while(N>0):
        p1=max(A)
        p2=max(B)
        if(p1>=p2 and X>0):
            result=result+p1
            t=A.index(p1)
            A.remove(A[t])
            B.remove(B[t])
            X=X-1
        else:
            result=result+p2
            t=B.index(p2)
            A.remove(A[t])
            B.remove(B[t])
            Y=Y-1
        N=N-1
    print(result)

if __name__ == "__main__":
    total = int(input())
    for i in range(0, total):
        Test()