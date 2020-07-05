a=[int(x) for x in input().split(',')]

def divide(x,y,z):
    if(len(x)==0):
        if(len(y)==0):
            mean1=0
        else:
            mean1=sum(y)/len(y)
        if(len(z)==0):
            mean2=0
        else:
            mean2=sum(z)/len(z)
        if(mean1==mean2):
            return True
        else:
            return False
    fir=x[0]
    x.remove(fir)
    y.append(fir)
    i=x.copy()
    j=y.copy()
    k=z.copy()
    if(divide(i,j,k)):
        return True
    y.remove(fir)
    z.append(fir)
    i=x.copy()
    j=y.copy()
    k=z.copy()
    if(divide(i,j,k)):
        return True
    else:
        return False
    
print(divide(a,[],[]))