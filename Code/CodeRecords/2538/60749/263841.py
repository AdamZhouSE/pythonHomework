str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
str1=list(map(int,str1.split(",")))
str1=sorted(str1)
res=[]
for _ in range(0,len(str1)+1):
    res.append(_)
label=0
for x in range(0,len(str1)):
    if not str1[x] ==res[x]:
        label=1
        print(res[x])
        break
if label==0:
    print(res[-1])