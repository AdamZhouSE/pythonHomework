first=eval('['+input()+']')
second=eval('['+input()+']')
if len(first)<len(second):
    temp=first
    first=second
    second=temp
jinWei=0
result=[]
for i in range(len(first)):
    if i%2==0:
        if i < len(second):
            temp = jinWei + first[len(first) - i - 1] + second[len(second) - i - 1]
        else:
            temp = jinWei + first[len(first) - i - 1]
        if temp==3:
            result.append(1)
            jinWei=1
        elif temp==2:
            result.append(0)
            jinWei=1
        elif temp==1:
            result.append(1)
            jinWei=0
        elif temp==0:
            result.append(0)
            jinWei=0
        else:
            result.append(1)
            jinWei=-1
    else:
        if i < len(second):
            temp = -jinWei + first[len(first) - i - 1] + second[len(second) - i - 1]
        else:
            temp = -jinWei + first[len(first) - i - 1]
        if temp==3:
            result.append(1)
            jinWei=-1
        elif temp==2:
            result.append(0)
            jinWei=-1
        elif temp==1:
            result.append(1)
            jinWei=0
        elif temp==0:
            result.append(0)
            jinWei=0
        else:
            result.append(1)
            jinWei=1
if jinWei==1:
    result.append(1)
    result.append(1)
elif jinWei==-1:
    result.append(0)
    result.append(1)
result.reverse()
judge=True
while result[0]==0:
    del result[0]
print(result)