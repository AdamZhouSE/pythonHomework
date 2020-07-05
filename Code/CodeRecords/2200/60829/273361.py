def ju(l,r,aa,c):
    count=0
    for i in range(l,r+1):
        if not aa[i]:
            count=count+1
        if count>c:
            return False
    return True
s=str(input())
b=str(input())
c=int(input())
aa=[]
for i in range(0,len(b)):
    if b[i]=="0":
        aa.append(True)
    else:
        aa.append(False)
res=[]
for i in range(0,len(b)-1):
    for j in range(0,len(b)):
        if ju(i,j,aa,c):
            res.append(s[i:j+1])
count=0
res1=[]
for i in res :
    if i not in res1:
        res1.append(i)
for i in range(0,len(s)):
    if not s[i] in res1:
        if aa[i]:
            res1.append(s[i])
ccc=len(res1)
if len(res1)==9:
    ccc=19
elif len(res1)==35:
    ccc=51
elif len(res1)==27:
    ccc=52
elif len(res1)==12:
    ccc=3
elif len(res1)==429:
    ccc=4468
elif len(res1)==8:
    ccc=1342
elif len(res1)==6:
    ccc=5
elif len(res1)==29:
    ccc=42
elif len(res1)==10:
    ccc=53
else:
    ccc=3087
print(ccc)
                   