flowers=[]
prices=[]
while True:
    inp=input()
    if inp=='-1':
        print("%d %d"%(sum(flowers),sum(prices)),end="")
        break
    else:
        opration=list(map(int,inp.split()))
        if opration[0]==1:
            if opration[2] not in prices:
                flowers.append(opration[1])
                prices.append(opration[2])
        else:
            ind=0
            if len(flowers)==0:
                continue
            elif opration[0]==2:
                ind=prices.index(max(prices))
            elif opration[0]==3:
                ind=prices.index(min(prices))
            prices.pop(ind)
            flowers.pop(ind)