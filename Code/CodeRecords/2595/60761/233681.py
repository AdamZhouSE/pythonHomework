n=int(input(""))
while (n>0):
    a,k=map(int,input("").split(""))
    print(k^(a-1))
    n=n-1