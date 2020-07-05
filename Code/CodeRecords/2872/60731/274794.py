num=int(input())
str=input()
res=[]
for i in range(num-1):
    if str[i]!=str[i+1]:
       res.append(str[i])
res.append(str[num-1])
num1=num-len(res)
print(res)
print(num1)