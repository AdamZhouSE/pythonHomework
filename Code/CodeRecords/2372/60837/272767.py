def priceDifference(a,b):
    result=[]
    for i in range(len(a)):
        result.append(a[i]-b[i])
    return result

def findMax(priceDifference,a,b,x,y):
    result=0
    Abs=[]
    for i in range(len(priceDifference)):
        Abs.append(abs(priceDifference[i]))
    for i in range(len(Abs)):        
        if y>0 and x>0:
            iMax=Abs.index(max(Abs))
            if priceDifference[iMax]<0:
                result+=b[iMax]
                Abs[iMax]=-1
                y-=1
            else:
                result+=a[iMax]
                Abs[iMax]=-1
                x-=1
        elif y==0:
            for j in range(len(Abs)):
                if Abs[j]>=0:
                    result+=a[j]
            break
        elif x==0:
            for j in range(len(Abs)):
                if Abs[j]>=0:
                    result+=b[j]
            break
    return result

T=int(input())
for i in range(T):
    nxy=list(map(int,input().split(' ')))
    a=list(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))
    pricedifference=priceDifference(a,b)
    print(findMax(pricedifference,a,b,nxy[1],nxy[2]))