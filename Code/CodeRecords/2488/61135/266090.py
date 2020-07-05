input=input()
a=input.replace('[','')
b=a.replace(']','')
c=b.replace('\n','')
d=c.split(',')
e=list()
for x in range(0,len(d)):
    e.append(int(d[x]))
e.sort()
rig=len(e)//2
lef=len(e)-rig
result=list()
count=0
while count<rig:
    result.append(e[count])
    result.append(e[lef+count])
    count=count+1
if lef>rig:
    result.append(e[count])
print(result,end='\n')