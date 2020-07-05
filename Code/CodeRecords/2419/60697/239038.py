num=input()
sum=0
pro=1
for i in range(len(num)):
    pro=pro*(int(num[i]))
for i in range(len(num)):
    sum=sum+(int(num[i]))
print(pro-sum)
