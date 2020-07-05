num=list(input().split(","))
num[0]=num[0][1:len(num[0])]
num[-1]=num[-1][0:-1]
for i in range(len(num)):
    num[i]=int(num[i])
res=0
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>2*num[j]:
            res+=1
print(res)