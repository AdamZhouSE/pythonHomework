import random
s=set()
mp={}
num=p=b=h=[0 for i in range(100010)]
n,m,q=map(int,input().split(' '))
for i in range(1,n+1):
    num[i]=int(random.random()*random.random()%1000000000*(random.random()*random.random()%2000000000))
s.add(1)
for i in range(n+1):
    h[1]^=num[i]
    p[1]+=1
    b[i]=1
for i in range(1,q+1):
    c,x,y=input().split(' ')
    x,y=int(x),int(y)
    if c=='C':
        if b[x]==y:
            continue
        try:
            s.remove(b[x])
            s.remove(y)
        except:
            pass
        h[b[x]]^=num[x]
        p[b[x]]-=1
        if h[b[x]] in mp:
            s.add(b[x])
        h[y]^=num[x]
        p[y]+=1
        if h[y] in mp:
            s.add(y)
        b[x]=y
    elif c=='W':
        ans=0
        for k in list(s):
            if k<=y:
                mp[h[k]]=1
                ans+=p[k]
                s.remove(k)
        if ans==0:
            print(ans)
        else:
            print(ans+1)
	 	    

