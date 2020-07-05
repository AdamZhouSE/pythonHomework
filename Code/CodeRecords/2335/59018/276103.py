#a乘2 -1==b除以2 +1
#if b>a: b偶则b/2 b奇则b+1 直到b=a      （也可能b<a!!!）

a=int(input())
b=int(input())
count=0
if b==a:
    print(0)
elif b>a:
    while(b>a):
        if b%2==0:
            b=b/2
        else:
            b=b+1
        count=count+1   
    print(int(count+a-b))
else:
    print(int(a-b))
