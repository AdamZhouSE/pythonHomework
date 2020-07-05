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
    if(tl[0]=='C'):
        index=int(tl[1])-1
        numlist[index]=int(tl[2])
    else:
        start=int(tl[1])-1
        end=int(tl[2])
        k=int(tl[3])-1
        temp=numlist[start:end]
        temp.sort()
        print(temp[k])