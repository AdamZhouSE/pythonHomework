t=int(input())
ask=[0]*t
maxx=0
for _ in range(t):
    ask[_]=int(input())
    maxx=max(maxx,ask[_])
oddcnt,evencnt=1,2
oddst,evenst=1,2
connell=[]
while(len(connell)<maxx):
    for i in range(oddcnt):
        connell.append(oddst+2*i)
    oddst+=2*evencnt
    oddcnt+=2
    for i in range(evencnt):
        connell.append(evenst+2*i)
    evenst+=2*oddcnt
    evencnt+=2
for i in ask:
    for j in range(0,i):
        print(connell[j],end=' ')
    print()