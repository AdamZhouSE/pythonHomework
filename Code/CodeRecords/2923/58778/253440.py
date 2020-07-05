s=input()
sl=s.split( )
n=int(sl[0])
q=int(sl[1])
t=input()
tl=t.split( )
numlist=[]
for i in tl:
    numlist.append(int(i))
count=[]
for i in range(n):
    count.append(0)
for i in range(q):
    s=input()
    sl=s.split( )
    for j in range(int(sl[0])-1,int(sl[1])):
        count[j]=count[j]+1
#print(count)
count.sort()
numlist.sort()
sum=0
for i in range(len(count)):
    sum=sum+count[i]*numlist[i]
print(sum)