list=input()
res=[]
res.append(-10000)
res.append(10000)
for i in range(len(list)):
    for j in range(len(res)):
        if int(list[i])>=int(res[j]) and  int(list[i])<=int(res[j+1]):
            res.insert(j+1,list[i])
            break
res.pop(0)
res.pop(len(list))
print(res)