def test19():
    X=input().split(" ")
    n=int(X[0])
    d=int(X[1])
    x=input().split(" ")
    num=0
    b=[]
    for i in x:
        b.append(int(i))
    for i in range(1,n):
        if b[i-1]>=b[1]:
            while True:
                if b[i-1]<b[i]:
                    break
                b[i]=b[i]+d
                num=num+1
    print(num)
test19()