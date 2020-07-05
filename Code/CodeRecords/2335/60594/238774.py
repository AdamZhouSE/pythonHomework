a=(int)(input())
b=(int)(input())
if a>b:
    print(a-b)
else:
    n=0
    while (a < b):
        if b % 2 == 1:
            b+=1
        else:
            b /= 2
        n+=1
    n+= a - b
    print((int)(n))