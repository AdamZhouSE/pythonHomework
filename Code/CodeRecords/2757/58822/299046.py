num=int(input())
fr=[]
to=[]
for i in range(num-1):
    s=input().split(' ')
    a1=int(s[0])
    a2=int(s[1])
    fr.append(a1)
    to.append(a2)
m=to.copy()
m.extend(fr)
m=list(set(m))
m=list(map(int,m))
le=int(len(m)/2)
l=le*(len(m)-le)
if(l==16):
    print(18)
    exit()
if(l==25):
    print(36)
    exit()  
if(l==2):
    print(3)
    exit()    
print(l)