num1=list(input().split(","))
num2=list(input().split(","))
num1[0]=num1[0][1:len(num1[0])]
num1[-1]=num1[-1][0:-1]
num2[0]=num2[0][1:len(num2[0])]
num2[-1]=num2[-1][0:-1]
for i in range(len(num1)):
    num1[i]=int(num1[i])
for i in range(len(num2)):
    num2[i]=int(num2[i])
res=[]
for i in num2:
    while i in num1:
        res.append(i)
        num1.remove(i)
res=res+sorted(num1)
print(res)