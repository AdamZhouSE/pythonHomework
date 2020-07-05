str=input()[1:-1]
afterStr=list()
num=0
i=0
while i<len(str):
    if str[i]=='[':
        j=i+2
        i=j+1
        while str[i]!='\"':
            i=i+1
        temp1=str[j:i]
        j=i+1
        while str[j] != '\"':
            j = j + 1
        j=j+1
        i = j + 1
        while str[i] != '\"':
            i = i + 1
        temp2=str[j:i]
        afterStr.append([temp1,temp2])
        num=num+1
    i=i+1
Depart="JFK"
res=list()
res.append(Depart)
i=0
while i<num-1:
    min=i
    j=i+1
    while j<num:
        if afterStr[i][0]==afterStr[j][0] and afterStr[min][1]>afterStr[j][1]:
            min=j
        j=j+1
    if min!=i:
        afterStr[min],afterStr[i]=afterStr[i],afterStr[min]
    i=i+1
i=0
while len(afterStr)!=0:
    if afterStr[i][0]==Depart:
        Depart=afterStr[i][1]
        afterStr.remove(afterStr[i])
        res.append(Depart)
        i=0
        continue
    i=i+1
print(res)