import functools

def add(l1,l2):
    l=[]
    l.append(l1[0]*l2[1]+l1[1]*l2[0])
    l.append(l1[1]*l2[1])
    if(l2[1]<0):
        l[0]=-l[0]
        l[1]=-l[1]
    i=min(l)
    if i==0:
        return [0,1]
    elif abs(i)==1:
        return l
    else:
        while i>1:
            if l[0]%i==0 and l[1]%i==0:
                l[0]/=i
                l[1]/=i
                i=min(i-1,min(l))
            else:
                i-=1
        return l


s=input().split('+')
l=[]
if s[0][0]=='-':
    tmp=s[0]
    del s[0]
    tmp=tmp.split('-')[1:]
    l+=list(map(lambda x:[-int(x.split('/')[0]),int(x.split('/')[1])],tmp))
for i in s:
    tmp=i.split('-')
    l.append(list(map(int,tmp.pop(0).split('/'))))
    l += list(map(lambda x: [-int(x.split('/')[0]), int(x.split('/')[1])], tmp))
res=functools.reduce(add,l)
print(str(res[0])+'/'+str(res[1]))def area(a,b,c):
    x=(a[0]-b[0],a[1]-b[1])
    y=(a[0]-c[0],a[1]-c[1])
    return abs(x[0]*y[1]-x[1]*y[0])/2.0

def maxArea(alist):
    max = 0.0
    n=len(alist)
    alist=list(set(alist))
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(max<area(alist[i],alist[j],alist[k])):
                    max = area(alist[i],alist[j],alist[k])


    return max

n=int(input())
alist = []
for i in range(n):
    location = tuple(map(int,input().split(',')))
    alist.append(location)
print(maxArea(alist))





