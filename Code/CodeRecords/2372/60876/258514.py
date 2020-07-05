n=int(input())
for i in range(0,n):
    N, X, Y = map(int, input().split(" "))
    As = list(map(str, input().split(" ")))
    B = list(map(int, input().split(" ")))
    A=[]
    for item in As:
        if item!="":
            A.append(int(item))
    Agap=[]
    Bgap=[]
    sum=0
    for ind in range(0,N):
        if A[ind]>B[ind]:
            Agap.append(A[ind]-B[ind])
            sum+=A[ind]
        else:
            Bgap.append(B[ind]-A[ind])
            sum+=B[ind]
    Agap.sort()
    Bgap.sort()
    lengthA=len(Agap)
    lengthB=len(Bgap)
    if lengthA>X:
        m=lengthA-X
        for j in range(0,m):
            sum-=Agap[j]
    elif lengthB>Y:
        m=lengthB-Y
        for j in range(0,m):
            sum-=Bgap[j]
    print(sum)