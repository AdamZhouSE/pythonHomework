n=int(input())
res=[]
li=[]
li.append(n)
res.append(li)
c=0
for i in range(5):
    ress=[]
    for j in range(len(res)):
        if res[j][-1]%2==0:
            temp = []
            for k in range(len(res[j])):
                temp.append(res[j][k])
            if int(res[j][-1]/2) not in res[j]:
                temp.append(int(res[j][-1]/2))
            ress.append(temp)
        else:
            if res[j][-1]+1 not in res[j]:
                temp = []
                for k in range(len(res[j])):
                    temp.append(res[j][k])
                temp.append(res[j][-1] + 1)
                ress.append(temp)
            if res[j][-1] - 1 not in res[j]:
                temp = []
                for k in range(len(res[j])):
                    temp.append(res[j][k])
                temp.append(res[j][-1] - 1)
                ress.append(temp)
    res=[]
    for i in ress:
        res.append(i)
    for i in res:
        if 1 in i:
            c=1
    if c==1:
        break
print(len(res[0])-1)