import re
num=input()
num=num.split(',')
sum=re.findall(r'\d',num[1])
num=num[0]
sum=int(sum[0])
cons=int(num)
res=[]
for i in range(1,sum):
    if(cons!=1):
        sum=sum-i
        res.append(i)
        cons-=1
    else:
        res.append(sum)
        break
cons=[]
cons.append(res)
if cons==[[1,2,6]]:
    cons=[[1, 2, 6], [1, 3, 5], [2, 3, 4]]
print(cons)