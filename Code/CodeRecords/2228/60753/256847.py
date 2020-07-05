target=input()
n=0
if target<0:
    target=-target
while int(n*(1+n)/2) < target:
    n+=1
if int(n*(1+n)/2)==target:
    print(n)
else:
    if (int(n*(1+n)/2)-target)%2==0:
        print(n)
    else:
        if n%2==0:
            print(n+1)
        else:
            print(n+2)