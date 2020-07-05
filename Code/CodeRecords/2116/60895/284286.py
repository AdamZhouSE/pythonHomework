n=int(input())
s=input().split(',')
num=[]
result=[]
result.append(1)
for item in s:
    num.append(int(item))
i=2
while len(result)<=n:
    temp=i
    while temp>1:
        k=temp
        for item in num:
            if temp%item==0:
                temp=temp//item
                break
        if temp==k:
            break
    if temp==1:
        result.append(i)
    i=i+1
print(result[n-1])