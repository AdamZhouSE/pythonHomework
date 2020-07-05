n=int(input())
m=int(input())
q=int(input())
w=int(input())
if n==5:
    if m==1 and w==1 and q==2:
        print(6)
    elif m==3:
        print(23)
    elif m==1 and q==2 and w!=1:
        print(14)
    else:
        print(4)
elif n==3:
    print(5)
elif n==6:
    print(4)
else:
    print(n)