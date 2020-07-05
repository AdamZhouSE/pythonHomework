def test2():
    X=input().split(" ")
    p=int(X[0])
    n=int(X[1])
    result=[]
    for i in range(p):
        result.append(0)
    for i in range(n):
        x=input();
        h=int(x)%p
        if result[h]==0:
            result[h]=1
        else:
            return i + 1
    return -1
print(test2())