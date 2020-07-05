A=list(input())
B=list(input())
C=list(input())
def maxAB(a,b):
    result=[]
    na=len(a)
    nb=len(b)
    nn=min(na,nb)
    for i in range(nn):
        if a[i]>b[i]:
            result=a
            break
        elif b[i]>a[i]:
            result=b
            break
        elif i==nn-1:
            result=a
    return result
    
def sortABC(a,b,c):
    new=[]
    if maxAB(a,b)!=a and maxAB(a,c)!=a:
        new.append(a)
        if max(b,c)!=b:
            new.append(b)
            new.append(c)
        else:
            new.append(c)
            new.append(b)
    elif maxAB(a,b)!=b and maxAB(b,c)!=b:
        new.append(b)
        if max(a,c)!=a:
            new.append(a)
            new.append(c)
        else:
            new.append(c)
            new.append(a)
    elif maxAB(a,c)!=c and maxAB(b,c)!=c:
        new.append(c)
        if max(a,b)!=a:
            new.append(a)
            new.append(b)
        else:
            new.append(b)
            new.append(a)
    for i in range(3):
        print(''.join(new[i]))
    return 0
sortABC(A,B,C)
                
                
                
                
                
                
                
           