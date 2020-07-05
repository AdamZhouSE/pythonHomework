s=input()
sl=s.split( )
q=int(sl[1])
n=input()
nl=n.split( )
numlist=[]
for i in nl:
    numlist.append(int(i))

for i in range(q):
    m=input()
    ml=m.split( )
    p=int(ml[0])-1
    b=int(ml[1])
    temp = numlist.copy()
    temp[p]=b
    numlist=temp.copy()
    x=0
    while(len(temp)!=1):
        z = []
        if(x%2==0):
            for j in range(0,len(temp),2):
                z.append(temp[j]|temp[j+1])
            x=x+1
        else:
            for j in range(0,len(temp),2):
                z.append(temp[j]^temp[j+1])
            x=x+1
        temp=z
    print(temp[0])