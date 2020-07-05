n=int(input())
num=list(str(n))
res=0
for i in range(len(num)):
    for j in range(len(num)):
        if i==j:
            break
        tem=num[i]
        num[i]=num[j]
        num[j]=tem
        if int(''.join(num)) > n and int(''.join(num)) > res:
            res = int(''.join(num))
        tem=num[i]
        num[i]=num[j]
        num[j]=tem
if res==0:
    res=n
print(res)