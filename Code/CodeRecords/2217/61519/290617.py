n1=list(input().split(","))
n2=list(input().split(","))
n3=list(input().split(","))
n4=list(input().split(","))
for i in range(2):
    n1[i]=int(n1[i])
    n2[i]=int(n2[i])
    n3[i]=int(n3[i])
    n4[i]=int(n4[i])
d1=(n2[0]-n1[0])**2+(n2[1]-n1[1])**2
d2=(n3[0]-n1[0])**2+(n3[1]-n1[1])**2
d3=(n4[0]-n1[0])**2+(n4[1]-n1[1])**2
d4=(n2[0]-n3[0])**2+(n2[1]-n3[1])**2
d5=(n2[0]-n4[0])**2+(n2[1]-n4[1])**2
d6=(n3[0]-n4[0])**2+(n3[1]-n4[1])**2
num=[]
num.append(d1)
num.append(d2)
num.append(d3)
num.append(d4)
num.append(d5)
num.append(d6)
num.sort(reverse=True)
res=[]
for i in num:
    if i not in res:
        res.append(i)
if len(res)!=2:
    key=False
elif res[0]==res[1]*2:
    key=True
print(key)