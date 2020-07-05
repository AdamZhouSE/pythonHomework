n=int(input())
result=0
ls=input().split(" ")
ls=[int(x) for x in ls]
#先看所有数加起来是不是偶数
total=0
for i in range(n):
    total=total+ls[i]
if total%2==0:
    result=total
else:
    #减掉一个，一定有是偶数的，否则所有数加起来一定是偶
    for i in range(n):
        total=0
        for j in range(n):
            if j!=i:
                total=total+ls[j]
        if total%2==0 and total>result:
            result=total
print(result)
