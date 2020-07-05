import math
number=int(input())
lists=[]
source=[]
try:
    while(True):
        source.append(input().split(" "))
except(EOFError):
    pass
i=0
while(i<len(source)):
    count=0
    for a in range(i+1,len(source)):
        if(int(source[i][0])>int(source[a][0])):
            x=source[a][0]
            source[a][0]=source[i][0]
            source[i][0]=x
            count=count+1
            break
    if(count==0):
        i=i+1
for i in range(pow(2,number+1)):
    lists.append("*")
lists[0]=source[0][0]
lists[1]=source[0][1]
for i in source[1:]:
    for x in range(len(lists)):
        if(lists[x]==i[0]):
            if(lists[2*x+1]=="*"):
                lists[2*x+1]=i[1]
            else:
                lists[2*x+2]=i[1]
res=0
last_number=0
for i in range(len(lists)-1,-1,-1):
    if(lists[i]!="*"):
        last_number=i
        res=res+int(math.log(i+1,2))
        break
while((last_number!=1)&(last_number!=2)):
    last_number=int((last_number+1)/2)-1
for a in range(1,len(lists)):
    y=a
    while((y!=1)&(y!=2)):
        y=int((y+1)/2)-1
    if(y==last_number):
        lists[a]="*"
for i in range(len(lists)-1,-1,-1):
    if(lists[i]!="*"):
        last_number=i
        res=res+int(math.log(i+1,2))
        break
print(res)
      










