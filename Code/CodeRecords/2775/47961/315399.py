a=int(input())
for i in range(0,a):
    b=int(input())
    if b%3==0:
        x1=b//3-1
        x2=b//3
        x3=b//3+1
        print(x1,end=" ")
        print(x2,end=" ")
        print(x3)
    else:
        print(-1)