p=int(input())
q=int(input())
if p%q==0:
    if (p//q)%2==0:
        print(2)
    else:
        print(1)
elif 3*q==2*p:
    print(0)