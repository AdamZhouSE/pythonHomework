s=input()
lenth=len(s)
i=1
List=[s]
while i<lenth:
    str1=s[i:lenth] + s[0:i]
    List.append(str1)
    i+=1
List.sort()
res=""
i=0
while i<lenth:
    res=res+List[i][lenth-1]
    i+=1


print(res,end='')