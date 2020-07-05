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
            A.remove(A.index(p1))
            B.remove(A.index(p1))
            X=X-1
        else:
            result=result+p2
            A.remove(B.index(p2))
            B.remove(B.index(p2))
            Y=Y-1
        N=N-1
    print(result)

if __name__ == "__main__":
    total = int(input())
    for i in range(0, total):
        Test()