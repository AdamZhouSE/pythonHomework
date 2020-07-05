s=input()
sl=s.split( )
n=int(sl[0])
m=int(sl[1])
t=input()
tl=t.split( )
numlist=[]
for i in tl:
    numlist.append(int(i))
for i in range(m):
    t=input()
    tl=t.split( )
    start=int(tl[0])-1
    end=int(tl[1])
    k=int(tl[2])-1
    temp=numlist[start:end]
    temp.sort()
    print(temp[k])