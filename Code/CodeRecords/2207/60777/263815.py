def bre(x,n,l):
    if(n>0 and x==0):
        return False
    if(n==1 and x not in l):
        return True
    for i in range(x,0,-1):
        if(i in l):
            continue
        temp=l.copy()
        temp.append(i)
        if(bre(x-i,n-1,temp)):
            return True
        temp.remove(i)
    return False

t=int(input())

for i in range(t):
    temp=[int(x) for x in input().split()]
    if(bre(temp[0],temp[1],[])):
        print(1)
    else:
        print(0)