def test5():
    n=int(input())
    a=[]
    b=[]
    num=1;
    for i in range(n):
        x=input().split(" ")
        a.append(int(x[0]))
        b.append(int(x[1]))
        
    for i in range(1,n):
        if a[i-1]==a[i]:
            if b[i-1]==b[i]:
                num=num+1;
    return num
print(test5())