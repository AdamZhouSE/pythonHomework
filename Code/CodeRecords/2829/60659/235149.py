n=int(input())
num=input().split()
for x in range(n):
    num[x]=int(num[x])
num.sort()
if len(num)<=2:
    result=0
else:
    if (num[len(num)-2]-num[0])>(num[len(num)-1]-num[1]):
        result=num[len(num)-1]-num[1]
    else:
        result=num[len(num)-2]-num[0]
print(result)