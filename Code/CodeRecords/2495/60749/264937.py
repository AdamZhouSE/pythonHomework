
def judge(str1,str2):
    res1=[]
    res2=[]
    for h in str1:
        res1.append(h)
    for h in str2:
        res2.append(h)
    ans=""
    for h in res2:
        if h in res1:
            ans=ans+h
            res1.remove(h)
    if ans==str2:
        return True
    return False

str1=input()
str2=input()
str2=str2.strip("[")
str2=str2.strip("]")
str2=str2.split(",")
res=[]
temp=[]
for h in str2:
    h=h.strip('"')
    res.append(h)
for h in res:
    if judge(str1,h):
        temp.append(h)
result=[]
max1=0
for t in temp:
    max1=max(max1,len(t))
for t in temp:
    if len(t)==max1:
        result.append(t)
result=sorted(result)
print(result[0])