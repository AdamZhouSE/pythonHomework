s=input()
sl=s.split( )
n=int(sl[0])
d=int(sl[1])
numlist=[]
numlist.append(2)
for i in range(d-1):
    numlist.append(numlist[len(numlist)-1]**n+1)
if(d==1):
    print(1,end='')
elif d==0:
    print(1,end='')
else:
    print(numlist[len(numlist)-1]-numlist[len(numlist)-2],end='')