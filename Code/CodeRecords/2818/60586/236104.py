def test4():
    X=input().split(" ")
    n=int(X[0])
    x=int(X[1])
    chp=input().split(" ").sort()
    sum=0;
    for i in range(n):
        if x>=1:
            sum=sum+x*int(chp[i])
        else:
            sum=sum+int(chp[i])
        x=x-1
    return sum
print(test4())