str=input()
newstr=''
for item in str:
    if not item in newstr:
        newstr=newstr+item
time={}
for m in newstr:
    time[m]=0
    for n in str:
        if n==m:
            time[m]=time[m]+1
    str=str.replace(m,'')
result=""
for step in range(0,len(time)):
    maxletter=newstr[0]
    for item in newstr:
        if time[item]>time[maxletter]:
            maxletter=item
    for x in range(0,time[maxletter]):
        result=result+maxletter
    time.pop(maxletter)
    newstr=newstr.replace(maxletter,'')
print(result)