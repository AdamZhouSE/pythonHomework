    p,s=map(float,input().split())
    l=(p-(p*p-24*s)**0.5)/12
    h=p/4-2*l
    print("%.5f" %(l*l*h))
    t-=1