p=int(input())
q=int(input())
if p%q==0:
    if (p//q)%2==0:
        print(2)
    else:
        print(1)
else:
    print(0)