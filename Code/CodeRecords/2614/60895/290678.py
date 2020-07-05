t=int(input())
while t>0:
    n=int(input())
    t=t-1
    a=input().split(' ')
    b=input().split(' ')
    c=input().split(' ')
    num=0
    for i in range(0,n):
        temp=int(a[i])-int(b[i])
        for k in range(0,n):
            if temp==int(c[k]):
                num=num+1
    print(num)