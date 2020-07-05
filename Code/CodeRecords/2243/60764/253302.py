length=int(input())
dis=int(input())
gcd=max(dis,length)
if dis==0:
    print(0)
else:
    while True:
        if gcd%length==0 and gcd%dis==0:
            break
        gcd+=1
    n=int(gcd/length)
    r=int(gcd/dis)
    if r%2==0:
        print(2)
    else:
        if n%2==0:
            print(0)
        else:
            print(1)