s=input()
sl=s.split( )
n=int(sl[0])
can=int(sl[1])
before=[]
after=[]
dif=[]
for i in range(n):
    k=input()
    kl=k.split( )
    before.append(int(kl[0]))
    after.append(int(kl[1]))
    dif.append(int(kl[0])-int(kl[1]))
su=sum(before)
least=sum(after)
if(least>can):
    print(-1)
else:
    c=0
    while(su>can):
        t=max(dif)
        index=dif.index(t)
        su=su-t
        dif[index]=0
        c=c+1
    print(c)