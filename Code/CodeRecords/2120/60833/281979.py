def judgemax(n):
    x1=n//2
    x2=n-x1
    if(x1*x2>n):
        x1=judgemax(x1)
        x2=judgemax(x2)
        return x1*x2
    else:
        return n
x=int(input())
if(x==2):
    print(1)
elif(x==3):
    print(2)
else:
    print(judgemax(x))
