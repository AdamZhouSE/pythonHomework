def test15():
    x=input().split(" ")
    n=int(x[0])
    m=int(x[1])
    y=input().split(" ")
    z=input().split(" ")
    a=[]
    b=[]
    c=[]
    for item in y:
        a.append(int(item))
    for item in z:
        b.append(int(item))
    for item in b:
        num=0
        for i in a:
            if i<=item:
                num=num+1
        c.append(num)
    result=str(c[0])
    for i in range(1,m):
        result=result+" "+str(c[i])
    return result
print(test15())