a=int(input())
b=int(input())
c=int(input())
# order a<b<c
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
dis1,dis2=b-a,c-b
minsteps,maxsteps=0,0
if dis1*dis2==1:
    minsteps=0
elif dis1==2 or dis2==2 or dis1==1 or dis2==1:
    minsteps=1
else:
    minsteps=2
maxsteps=b-1-a+c-(b+1)
print([minsteps,maxsteps])