num=list(input().split(","))
for i in range(len(num)):
    num[i]=int(num[i])
num1=[]
for i in num:
    if i not in num1:
        num1.append(i)
num1.sort()
res=len(num1)
for i in range(len(num1)):
    res=res+num1[i]
print(res)