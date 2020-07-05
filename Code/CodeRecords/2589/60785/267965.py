t=int(input())
for i in range(t):
    a=0
    b=1
    num=[]
    n=int(input())
    while b>=1:
        num.append(b)
        a,b=b,a+b
        if len(num)==n:
            print(num[n-1])
    