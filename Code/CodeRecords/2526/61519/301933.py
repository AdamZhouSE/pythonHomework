num1=list(input().split(","))
num2=list(input().split(","))
num1[0]=num1[0][1:len(num1[0])]
num1[-1]=num1[-1][0:-1]
num2[0]=num2[0][1:len(num2[0])]
num2[-1]=num2[-1][0:-1]
res1=[]
res2=[]
for i in range(len(num1)):
    if num1[i]!="null":
        res1.append((num1[i]))
for i in range(len(num2)):
    if num2[i]!="null":
        res2.append((num2[i]))
res=[]
res=res1+res2
result=[]
for i in range(len(res)):
    if res[i]!='':
        result.append(int(res[i]))
result.sort()
print(result)