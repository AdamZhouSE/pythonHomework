def test4():
    X=input().split(" ")
    n=int(X[0])
    x=int(X[1])
    chp=input().split(" ")
    c=[]
    for item in chp:
        c.append(int(item))
    c.sort()
    sum=0;  
    for i in range(n):
        if x>=1:
            sum=sum+x*c[i]
        else:
            sum=sum+c[i]
        x=x-1
    return sum
print(test4())