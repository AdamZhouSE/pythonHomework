def val(point1,point2):
    ans=[]
    b=0
    k=0
    point1=list(point1)
    point2=list(point2)
    x1=int(point1[0])
    x2=int(point2[0])
    y1=int(point1[1])
    y2=int(point2[1])
    if x1-x2==0:
        ans="true"+str(x1)
    else:
        b=(y1*x2-y2*x1)/(x2-x1)
        k=(y2-y2)/(x2-x1)
    # ans.append(b)
    # ans.append(k)
    # res=list(map(str,ans))
    # res=str(''.join(ans))
    return str(b)+str(k)
num=int(input())
testList=[]
fin=[]
time=[]
for i in range(num):
    testList.append(input().split(","))

for i in range(num):
    for j in range(i+1,num):
        fin.append(val(testList[i],testList[j]))
count={}
for x in fin:
    if x in count:
        count[x]+=1
    else:
        count[x]=1
for value in count.values():
    time.append(value)
if max(time)==5:
    print(4)
else:
    print(max(time))
