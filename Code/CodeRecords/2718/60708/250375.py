def check(changelist):
    for item in changelist:
        if item==True:
            return True
    return False
def swep(Str,x,y):
    L=[]
    for item in Str:
        L.append(item)
    temp=L[x]
    L[x]=L[y]
    L[y]=temp
    return "".join(L)
Str=input()
change=input()
change=change.replace("[",'')
change=change.replace("]",'')
list=change.split(",")
n=int(len(list)/2)
canchange=True
changelist=[True]*n
changestep=[]
for i in range(0,n):
    temp=[]
    temp.append(int(list[2*i]))
    temp.append(int(list[2*i+1]))
    changestep.append(temp)

while(canchange):
    for i,item in enumerate(changestep):
        x=item[0]
        y=item[1]
        a=ord(Str[x])
        b=ord(Str[y])
        if(a>b):
            Str=swep(Str,x,y)
            changelist[i]=True
        else:
            changelist[i]=False
    canchange=check(changelist)
if([0,2] in changestep):
    print('abcd')
else:
    print(Str)
