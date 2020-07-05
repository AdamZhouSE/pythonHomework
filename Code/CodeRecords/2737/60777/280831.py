temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
x=(int)(len(temp)/3)
res=[]
for i in range(len(temp)):
    if(temp.count(temp[i])>x and not(temp[i] in res)):
        res.append(temp[i])

print(res)
