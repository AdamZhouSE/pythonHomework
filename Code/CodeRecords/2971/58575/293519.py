str=input()
res=list()
lengthStr=len(str)
i= lengthStr-1
temp=""
while i>=0:
    temp=str[i]+temp
    res.append(temp)
    i=i-1
res.sort()
i=0
while i<lengthStr:
    length=len(res[i])
    print(lengthStr-length+1,end=" ")
    i=i+1