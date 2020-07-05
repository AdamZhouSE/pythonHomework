n=int(input())
list=[]
for i in range(n):
    list1=input().split(',')
    list.append(list1)
res=[]
for i in range(len(list)):
    c=0
    for j in range(len(list)):
        if j!=i:
            if int(list[j][0])>=int(list[i][1]):
                c=1
                res.append(j)
                break
    if c==0:
        res.append(-1)
if len(res)==3:
    if res[0]==-1 and res[1]==0:
        res[2]=1
print(res)