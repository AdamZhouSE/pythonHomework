a=(int)(input())
n=1
while n<=a:
    li=input().split()
    x1=(int)(li[0])
    x2=(int)(li[1])
    yeshu=1
    n1=2
    while n1<=x1:
        yeshu=yeshu*x2
        n1+=1
    print(yeshu)
    n+=1
