n=int(input())
v=[int(x) for x in input().split(' ')]
a=[int(x)-1 for x in input().split(' ')]

def most(i,f,v,a,s):
    more=False
    temp=i
    while(f[a[temp]]!=-1 and temp!=i):
        temp=a[temp]
    if(f[a[temp]]==-1):
        more=True
    else:
        return s
    s+=v[a[temp]]
    f[a[temp]]=0
    temp=a[temp]
    return most(temp,f,v,a,s)

for i in range(n):
    temp=[-1]*n
    temp[i]=0
    print(most(i,temp,v,a,v[i]))