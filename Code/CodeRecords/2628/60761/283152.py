def gcd(a,b):
    if(a<b):
        a=a+b
        b=a-b
        a=a-b
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
#皮克定理：其面积S和内部格点数目a、边上格点数目b的关系s=a+b/2-1;a=s-b/2+1
t=int(input())
for i in range(t):
    x1,y1=map(int,input().split(" "))
    x2,y2=map(int,input().split(" "))
    x3,y3=map(int,input().split(" "))
    s=abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
    #利用gcd求边上的整数点数：一条线段（端点是整数坐标）上的整数点数-1是端点横坐标之差的绝对值和纵坐标之差绝对值的最大公约数。
    l1=gcd(abs(x1-x2),abs(y1-y2))
    l2=gcd(abs(x2-x3),abs(y2-y3))
    l3=gcd(abs(x3-x1),abs(y3-y1))
    b=l1+l2+l3
    print(int(s-b/2+1))