import re
n=int(input())
h=[]
v=[]
result=[]
for i in range(n*n):
    l=eval('['+input().replace(' ',',')+']')
    if l[0] not in h and l[1] not in v:
        h.append(l[0])
        v.append(l[1])
        result.append(i+1)
r=str(result)
r=re.sub("[\[\]]",'',r)
r=re.sub(",",'',r)
print(r)