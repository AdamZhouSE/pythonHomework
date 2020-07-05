num=list(input().split(","))
num[0]=num[0][1:len(num[0])]
num[-1]=num[-1][0:-1]
res=[]
for i in range(len(num)):
    num[i]=int(num[i])
key=0
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            key+=1
    res.append(key)
    key=0
res.append(0)
print(res)