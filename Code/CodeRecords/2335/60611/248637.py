x = int(input())
y = int(input())
operate=0
if x>=y:
    print(x-y)
else:
    while y%2==0 :
        y=y/2
        operate=operate+1
        if y<=x:
            break
    if y<=x:
        operate=operate+x-y
    else:
        while y>x:
            x=x*2
            operate=operate+1
        operate=operate+x-y
    print(int(operate))