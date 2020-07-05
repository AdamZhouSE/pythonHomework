def maxTip():
    test=int(input())
    for i in range(0,test):
        row1st=list(map(int, input().split(" ")))
        A=input().split(" ")
        B=input().split(" ")
        if not A[-1].isdigit():
            A.pop()
        if not B[-1].isdigit():
            B.pop()
        A=list(map(int, A))
        B=list(map(int, B))
        N=row1st[0]
        X=row1st[1]
        Y=row1st[2]
        calTip(N, X, Y, A, B)

def calTip(N, X, Y, A, B):
    AsubB=[]
    ATip=[]
    BTip=[]
    res=0
    for i in range(0, N):
        AsubB.append(A[i]-B[i])
    for i in range(0, X):
        if max(AsubB)<=0:
            break
        idx=AsubB.index(max(AsubB))
        ATip.append(idx)
        AsubB[idx]=0
    for i in range(0, N):
        if i not in ATip:
          BTip.append(i)
    for idx in ATip:
        res+=A[idx]
    for idx in BTip:
        res+=B[idx]
    print(res)

if __name__=='__main__':
    maxTip()
