import itertools
n=int(input())
list=[]
for m in range (n):
    num=int(input())
    list.append(num)
temp=[]
temp.append(-1)
temp.append(1)
templist=itertools.product(temp,repeat=n)
res=[]
for item in templist:
    res.append(item)
finalres=[]
for i in range(len(res)):
    m=0
    for j in range(n):
        m=m+int(list[j])*int(res[i][j])
    finalres.append(m)
c=0
for item in finalres:
    if int(item)==0 or int(item)==360:
        print("YES")
        c=1
        break
if c==0:
    print("NO")