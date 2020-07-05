import math
def whether(arr,i):
    res=True
    node=arr[i]
    if node=='null':
        return True
    l=len(arr)
    depth=0
    p=i*2
    while p<l:
        for j in range(p,p+int(math.pow(2,depth))):
            if arr[p]!='null':
                if arr[p]>node:
                    res = False
                    return res
        depth=depth+1
        p=p*2
    depth=0
    n=i*2+1
    while n<l:
        for j in range(n,n+int(math.pow(2,depth))):
            if arr[n]!='null':
                if arr[n]<node:
                    res = False
                    return res
        depth=depth+1
        n=n*2
    return True


s=input()
a=s[1:-1].split(',')
for i in range(0,len(a)):
    if a[i]!='null':
        a[i]=int(a[i])
a=[0]+a
ans=True
for i in range(1,len(a)):
    t=whether(a,i)
    if not t:
        break
if t:
    print('true')
else:
    print('false')
