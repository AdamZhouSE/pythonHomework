n,t = map(int,input().split())
a=[int(n) for n in input().split()]
number=0
for i in range(0,n):
    j=i
    time=0
    num=0
    while time<=t and j<=n-1:
        time+=a[j]
        num+=1
        j+=1
    if j==n and time<=t:
        if num > number:
            number = num
    else:
        if num-1>number:
            number=num-1

print(number)


        