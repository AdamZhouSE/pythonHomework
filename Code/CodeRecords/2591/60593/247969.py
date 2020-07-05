T=int(input())
q=[]
maxx=0
for tt in range(T):
    n=int(input())
    q.append(n)
    maxx=max(maxx,n)
chk={}
q1=7
q2=13
q3=5
while(True):
    chk[q1]=True
    chk[q2]=True
    chk[q3]=True
    q1+=6
    q2+=10
    q3+=14
    if(min(q1,q2,q3)>maxx):
        break
for i in q:
    if(i%2==0):
        print('No')
    else:
        if(i in chk):
            print('No')
        else:
            print('Yes')