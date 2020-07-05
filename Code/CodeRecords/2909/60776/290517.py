a=input()
list=[]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        list.append(a[i:j+1])
maxletter=int(input())
minsize=int(input())
maxsize=int(input())
result1=[]
for i in range(0,len(list)):
    if len(list[i])<=maxsize and len(list[i])>=minsize:
        result1.append(list[i])
result=[]
for i in range(0,len(result1)):
    count=[]
    for j in range(0,len(result1[i])):
        if result1[i][j] not in count:
            count.append(result1[i][j])
    if len(count)<=maxletter:
        result.append(result1[i])
newresult=[]
for i in range(0,len(result)):
    if result[i] not in newresult:
        newresult.append(result[i])
max=0
for i in range(0,len(newresult)):
    temp=[]
    temp.extend(result)
    while(newresult[i] in temp):
        temp.remove(newresult[i])
    if len(result)-len(temp)>max:
        max=len(result)-len(temp)
print(max)