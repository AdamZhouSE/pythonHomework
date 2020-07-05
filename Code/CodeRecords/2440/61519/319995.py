num=list(input().split(","))
num[0]=num[0][1:len(num[0])]
num[-1]=num[-1][0:-1]
for i in range(len(num)):
    num[i]=int(num[i])
num.sort()
print(num)