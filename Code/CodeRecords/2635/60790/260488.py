def zeta(x):
    return x/5+zeta(x/5) if x>0 else 0
k=int(input())
lo,hi=k,10*k+1
j=True
while(lo<hi):
    mi=(lo+hi)/2
    zmi=zeta(mi)
    if (zmi==k):
        j=False
        print(5)
        break
    elif(zmi<k):
        lo=mi+1
    else:
        hi=mi
if(j):
    print(0)