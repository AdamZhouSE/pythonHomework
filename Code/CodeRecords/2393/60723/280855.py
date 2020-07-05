T=int(input())
for i in range(T):
    temp=input().split()
    M=int(temp[0])
    N=int(temp[1])
    temp=input().split()
    arrayX=[]
    for j in range(M):
        arrayX.append(int(temp[j]))
    temp=input().split()
    arrayY=[]
    for j in range(N):
        arrayY.append(int(temp[j]))
    count=0
    for j in range(M):
        for k in range(N):
            if pow(arrayX[j],arrayY[k])>pow(arrayY[k],arrayX[j]):
                count=count+1
    print(count)