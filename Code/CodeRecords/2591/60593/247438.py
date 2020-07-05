T=int(input())
q=[]
maxx=0
for tt in range(T):
    n=int(input())
    q.append(n)
    maxx=max(maxx,n)
beg=3
cnt=2
sav={}
while(True):
    for i in range(0,cnt+1):
        beg=max(beg,beg+i*2)
        sav[beg]=True
    cnt+=2
    if(beg>maxx):
        break
for i in q:
    print('Yes'if sav[i] else'No')
