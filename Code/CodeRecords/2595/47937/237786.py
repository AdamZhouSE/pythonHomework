n=int(input())

i=0
while i<n:
    s=input().split(" ")
    a=int(s[0])
    b=int(s[1])
    i2=1
    num=1
    while i2<a:
        num=num*b
        i2=i2+1
    print(num)
    i=i+1

