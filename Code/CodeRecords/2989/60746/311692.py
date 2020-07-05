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
    new=[a,b,c]
    for i in range(2):
        for j in range(i+1):
            if maxAB(new[i],new[j])==new[i]:
                t=new[i]
                new[i]=new[j]
                new[j]=t
    for i in range(3):
        print(''.join(new[i]))
    return 0

sortABC(A,B,C)
                
                
                
                
                
                
                
                