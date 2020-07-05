t=int(input(""))
while(t>0):
    n,k=map(int,input("").split(" "))
    print(k**(n-1))
    t=t-1