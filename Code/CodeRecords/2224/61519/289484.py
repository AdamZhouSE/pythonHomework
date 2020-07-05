n=int(input())
num=list(str(n))
res=0
for i in range(len(num)):
    for j in range(len(num)):
        if i==j:
            break
        num[i]=num[j]
        num[j]=num[i]
        if int(''.join(num)) > n and int(''.join(num)) > res:
            res = int(''.join(num))
        num[i],num[j] = num[j],num[i]
if res==0:
    res=n
print(res)