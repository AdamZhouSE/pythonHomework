def exam9():
    X=input().split(" ")
    n=int(X[0])
    m=int(X[1])
    Y=input().split(" ")
    num=[]
    for i in range(n):
        num.append(int(Y[i]))
    for i in range(m):
        z=input().split(" ")
        if z[0]=="0":
            num[int(z[1])-1:int(z[2])]=sorted(num[int(z[1])-1:int(z[2])])
        else:
            num[int(z[1]) - 1:int(z[2])]=sorted(num[int(z[1])-1:int(z[2])],reverse=True)
    q=int(input())
    print(num[q-1])
exam9()