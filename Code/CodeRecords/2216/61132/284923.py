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
print(str(int(res[0]))+'/'+str(int(res[1])))